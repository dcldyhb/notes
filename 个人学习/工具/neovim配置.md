# neovim 配置

## $LaTeX$ 相关

可以，按你现在这套 **macOS + Neovide + LazyVim + Skim**，最稳的方案不是照抄文章里的 **UltiSnips + Zathura**，而是：

1. 用 **LazyVim 官方 TeX extra** 把 **VimTeX** 接进来；
2. 用 **VimTeX + Skim** 做编译、forward search、inverse search；
3. 保留你仓库里已经有的 `snippets/latex.json` 这类**静态** snippets；
4. 把 Castel 文章里真正关键的 **regex / context / postfix / autosnippets** 迁到 **LuaSnip 的 Lua snippets**。

这是因为你当前仓库里还没开 TeX extra，`lazyvim.json` 的 `extras` 也是空的；你已经在 `lua/plugins/snippets.lua` 里用 LuaSnip 从 `snippets/` 目录加载 VSCode 风格 snippets，`snippets/latex.json` 里也已经有方程、积分、分式这些基础片段。但 Castel 那篇文章的核心并不是这些静态模板，而是 **VimTeX 的语法上下文 + 高级 snippet 逻辑**。另外，blink 官方文档说明它默认用的是 `vim.snippet`；要用 LuaSnip 的高级能力，需要把 preset 切到 `luasnip`。([GitHub][1])

### 1）先把 LazyVim 的 TeX extra 打开

你现在的 `lua/config/lazy.lua` 里已经有 `prettier` 的 extra，直接再加一行最省事：

```lua
-- lua/config/lazy.lua
require("lazy").setup({
  spec = {
    { "LazyVim/LazyVim", import = "lazyvim.plugins" },
    { import = "lazyvim.plugins.extras.formatting.prettier" },
    { import = "lazyvim.plugins.extras.lang.tex" }, -- 新增
    { import = "plugins" },
  },
  -- 下面保持你原来的内容
})
```

这一步很重要，因为 LazyVim 官方这个 extra 已经帮你做了三件关键事：
它会加上 **VimTeX**，并且明确把它设成 **不要 lazy-load**（否则 inverse search 会坏）；还会给 Tree-sitter 安装 `latex/bibtex` parser，但同时**禁用 latex 的 Tree-sitter 高亮**。后一点正好对应 VimTeX 文档里的说明：像 `vimtex#syntax#in_mathzone()` 这类功能依赖的是 Vim 的内建 syntax 解析，不是 Tree-sitter；如果 LaTeX 高亮完全交给 Tree-sitter，很多 VimTeX 功能会失效。([GitHub][2])

### 2）给 VimTeX 加一层 macOS / Skim 配置

新建文件：

```lua
-- lua/plugins/vimtex.lua
return {
  {
    "lervag/vimtex",
    init = function()
      vim.g.tex_flavor = "latex"

      -- PDF viewer: Skim
      vim.g.vimtex_view_method = "skim"
      vim.g.vimtex_view_skim_sync = 1
      vim.g.vimtex_view_skim_activate = 1

      -- 不要老弹 quickfix
      vim.g.vimtex_quickfix_mode = 0

      -- 文章里用的是旧的 g:tex_conceal；在当前 VimTeX 里用这个
      vim.g.vimtex_syntax_conceal = {
        accents = 1,
        ligatures = 1,
        cites = 1,
        fancy = 1,
        texTabularChar = 1,
        spacing = 1,
        greek = 1,
        math_bounds = 1,
        math_delimiters = 1,
        math_fracs = 1,
        math_super_sub = 1,
        math_symbols = 1,
        sections = 0,
        styles = 1,
      }

      vim.api.nvim_create_autocmd("FileType", {
        pattern = { "tex", "plaintex", "bib" },
        callback = function()
          vim.opt_local.conceallevel = 2
          vim.opt_local.concealcursor = "nc"
        end,
      })

      -- 如果你的 LaTeX 模板统一走 xelatex，可打开这段
      -- vim.g.vimtex_compiler_latexmk = {
      --   options = {
      --     "-xelatex",
      --     "-synctex=1",
      --     "-interaction=nonstopmode",
      --     "-file-line-error",
      --   },
      -- }
    end,
  },
}
```

Castel 文章里的 conceal 配置还是 `set conceallevel=1` + `g:tex_conceal='abdmg'` 那一代写法；当前 VimTeX 文档公开配置的是 `g:vimtex_syntax_conceal`，并且说明 **conceal 要正常工作最好把 `conceallevel` 设到 2**。如果你更喜欢文章里那种“只稍微隐藏一点”的视觉效果，可以把上面的 `2` 改回 `1`。([Castel][3])

### 3）把 blink 切到 LuaSnip preset

你现在 `lua/plugins/blink.lua` 里虽然保留了 `snippets` source，但官方文档说 **blink 默认用的是 `vim.snippet`**；要让它真正按 LuaSnip 的方式做展开和跳转，需要显式设成 `preset = "luasnip"`。([Blink Completion][4])

你现有文件里只要补这一行：

```lua
-- lua/plugins/blink.lua
return {
  "saghen/blink.cmp",
  opts = function(_, opts)
    opts.snippets = { preset = "luasnip" } -- 新增

    -- 你原来的配置继续保留
    opts.sources = {
      default = { "lsp", "path", "snippets" },
      providers = {
        buffer = { enabled = false },
      },
    }

    -- 下面照旧
    return opts
  end,
}
```

### 4）把现有 LuaSnip 配置升级成“JSON + Lua snippets 混合加载”

你仓库里现在 `lua/plugins/snippets.lua` 只加载 `snippets/` 下面的 VSCode JSON。保留它，再加一个 Lua loader，并打开 autosnippets。LuaSnip 官方文档也明确说：**VSCode/JSON 更简单，但 Lua snippets 更强**；而 autosnippets 默认是关闭的，需要手动开。([GitHub][5])

把 `lua/plugins/snippets.lua` 改成这样：

```lua
-- lua/plugins/snippets.lua
return {
  {
    "L3MON4D3/LuaSnip",
    keys = function()
      return {}
    end,
    opts = function()
      local ls = require("luasnip")

      ls.config.set_config({
        enable_autosnippets = true,
        region_check_events = "InsertEnter,CursorMoved",
        delete_check_events = "TextChanged,InsertLeave",
      })

      -- 继续保留你现在的 JSON snippets
      require("luasnip.loaders.from_vscode").lazy_load({
        paths = { vim.fn.stdpath("config") .. "/snippets" },
      })

      -- 新增：加载 Lua snippets（高级逻辑放这里）
      require("luasnip.loaders.from_lua").lazy_load({
        paths = { vim.fn.stdpath("config") .. "/lua/snippets" },
      })
    end,
  },
}
```

### 5）把 Castel 的核心高级片段迁到 `lua/snippets/tex.lua`

新建文件：

```lua
-- lua/snippets/tex.lua
local ls = require("luasnip")
local s = ls.snippet
local t = ls.text_node
local i = ls.insert_node
local f = ls.function_node

local extras = require("luasnip.extras")
local rep = extras.rep
local fmta = require("luasnip.extras.fmt").fmta
local postfix = require("luasnip.extras.postfix").postfix

local function has_vimtex_fun(name)
  return vim.fn.exists("*" .. name) == 1
end

local function in_math()
  return has_vimtex_fun("vimtex#syntax#in_mathzone")
    and vim.fn["vimtex#syntax#in_mathzone"]() == 1
end

local function in_comment()
  return has_vimtex_fun("vimtex#syntax#in_comment")
    and vim.fn["vimtex#syntax#in_comment"]() == 1
end

local function math()
  return in_math() and not in_comment()
end

local function text()
  return not in_math() and not in_comment()
end

return {
  -- beg -> begin/end
  s({
    trig = "beg",
    name = "begin/end",
    wordTrig = true,
    snippetType = "autosnippet",
    condition = text,
  }, fmta([[
\begin{<>}
  <>
\end{<>}
]], { i(1), i(0), rep(1) })),

  -- mk -> inline math
  s({
    trig = "mk",
    name = "inline math",
    wordTrig = true,
    snippetType = "autosnippet",
    condition = text,
  }, fmta("$<>$<>", { i(1), i(0) })),

  -- dm -> display math
  s({
    trig = "dm",
    name = "display math",
    wordTrig = true,
    snippetType = "autosnippet",
    condition = text,
  }, fmta([[
\[
  <>
.\]
<>
]], { i(1), i(0) })),

  -- a1 -> a_1
  s({
    trig = "([A-Za-z])(%d)",
    regTrig = true,
    wordTrig = false,
    snippetType = "autosnippet",
    condition = math,
  }, f(function(_, snip)
    return snip.captures[1] .. "_" .. snip.captures[2]
  end, {})),

  -- a_12 -> a_{12}
  s({
    trig = "([A-Za-z])_(%d%d)",
    regTrig = true,
    wordTrig = false,
    snippetType = "autosnippet",
    condition = math,
  }, f(function(_, snip)
    return snip.captures[1] .. "_{" .. snip.captures[2] .. "}"
  end, {})),

  -- superscripts
  s({
    trig = "sr",
    name = "^2",
    wordTrig = true,
    snippetType = "autosnippet",
    condition = math,
  }, t("^2")),

  s({
    trig = "cb",
    name = "^3",
    wordTrig = true,
    snippetType = "autosnippet",
    condition = math,
  }, t("^3")),

  s({
    trig = "compl",
    name = "complement",
    wordTrig = true,
    snippetType = "autosnippet",
    condition = math,
  }, t("^{c}")),

  s({
    trig = "td",
    name = "superscript",
    wordTrig = true,
    snippetType = "autosnippet",
    condition = math,
  }, fmta("^{<>}<>", { i(1), i(0) })),

  -- 普通前缀 bar / hat
  s({
    trig = "bar",
    name = "overline",
    priority = 10,
    wordTrig = true,
    snippetType = "autosnippet",
    condition = math,
  }, fmta("\\overline{<>}<>", { i(1), i(0) })),

  s({
    trig = "hat",
    name = "hat",
    priority = 10,
    wordTrig = true,
    snippetType = "autosnippet",
    condition = math,
  }, fmta("\\hat{<>}<>", { i(1), i(0) })),

  -- postfix: zbar -> \overline{z}, phat -> \hat{p}
  postfix({
    trig = "bar",
    name = "overline postfix",
    priority = 100,
    snippetType = "autosnippet",
    condition = math,
  }, {
    f(function(_, parent)
      return "\\overline{" .. parent.snippet.env.POSTFIX_MATCH .. "}"
    end, {}),
  }),

  postfix({
    trig = "hat",
    name = "hat postfix",
    priority = 100,
    snippetType = "autosnippet",
    condition = math,
  }, {
    f(function(_, parent)
      return "\\hat{" .. parent.snippet.env.POSTFIX_MATCH .. "}"
    end, {}),
  }),
}
```

这份 Lua snippets 覆盖的是 Castel 文章里最关键、也是 **JSON snippets 做不好的那部分**：
`beg`、`mk/dm`、`a1 -> a_1`、`sr/cb/td`、以及 `zbar/phat` 这种 postfix 形式。文章里强调的“根据是不是 math zone 决定能不能展开”，也是靠 `vimtex#syntax#in_mathzone()` 实现的。([Castel][3])

你原来 `snippets/latex.json` 里的 `Equation / Integral / Fraction` 这些静态模板可以继续留着，不需要重写；Lua 文件只管高阶逻辑。([GitHub][6])

### 6）Skim 里把 inverse search 配好

在 **Skim → Settings / Preferences → Sync** 里这样填：

- **Preset**: `Custom`
- **Command**: 填 `which nvim` 的实际结果
- **Arguments**:

  ```bash
  --headless -c "VimtexInverseSearch %line '%file'"
  ```

然后在 PDF 里用 **Shift + Command + 点击** 做反查。

这是 VimTeX 官方给 Skim 的推荐配置，Skim 自己的同步文档也说明了 `%line` / `%file` 这两个占位符以及 `Shift-Command-click` 的触发方式。VimTeX 文档还特别提到，在某些系统里最好直接写 Neovim 的完整路径。([GitHub][7])

### 7）如何验证

打开一个 `test.tex`：

```tex
\documentclass{article}
\begin{document}
hello mk
x1 sr zbar phat
dm
\end{document}
```

然后在 Neovim 里执行：

```vim
:VimtexCompile
:VimtexView
```

你应该能得到这些效果：

- `mk` 展开成行内数学；
- `dm` 展开成 display math；
- `x1` 自动变 `x_1`；
- `sr` 变 `^2`；
- `zbar` / `phat` 变 postfix 数学片段；
- Skim 里 `Shift + Cmd + Click` 能跳回 Neovim。

如果编译器或 viewer 没起来，VimTeX README 里给了两个直接的排错入口：`<localleader>li` 看启动命令，`<localleader>lo` 看编译输出。([GitHub][8])

### 8）如果 Skim 反查还是不工作

先在 Neovim 里看：

```vim
:echo v:servername
```

Neovim 官方文档说，启动时通常会创建默认 RPC socket，并把地址放进 `v:servername`；如果需要，也可以显式用 `--listen` 指定地址。换句话说，这里**不应该是空的**。如果是空的，再去排查你当前启动方式，必要时显式 `--listen` 或在配置里 `serverstart()`。([Neovim][9])

---

按上面改完，你这套环境就能得到和文章**同一类体验**：

- **Neovide** 负责编辑；
- **Skim** 负责 PDF 预览和反查；
- **VimTeX** 负责编译、synctex、math context、conceal；
- **LuaSnip** 负责把 Castel 文里的 UltiSnips 逻辑迁成你现在仓库更适合的实现。

唯一不是 1:1 复刻的地方，是我建议你把文章里最复杂的那几个片段（比如“智能空格的 `mk`”和“`(...)/` 自动找匹配括号的分式”）放到第二阶段再做；因为这两类逻辑在 LuaSnip 里也能做，但代码会明显更长。先把上面这套跑通，已经能覆盖文章核心工作流的大部分。

如果你愿意，我下一条可以直接按你这个 repo 的文件结构，给你一份“可复制的完整 diff 版”。

[1]: https://raw.githubusercontent.com/dcldyhb/nvim-config-mac/main/lazyvim.json "https://raw.githubusercontent.com/dcldyhb/nvim-config-mac/main/lazyvim.json"
[2]: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/plugins/extras/lang/tex.lua "https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/plugins/extras/lang/tex.lua"
[3]: https://castel.dev/post/lecture-notes-1/?from=hackcv "https://castel.dev/post/lecture-notes-1/?from=hackcv"
[4]: https://cmp.saghen.dev/configuration/snippets "https://cmp.saghen.dev/configuration/snippets"
[5]: https://github.com/L3MON4D3/LuaSnip "https://github.com/L3MON4D3/LuaSnip"
[6]: https://raw.githubusercontent.com/dcldyhb/nvim-config-mac/main/snippets/latex.json "https://raw.githubusercontent.com/dcldyhb/nvim-config-mac/main/snippets/latex.json"
[7]: https://raw.githubusercontent.com/lervag/vimtex/master/doc/vimtex.txt "https://raw.githubusercontent.com/lervag/vimtex/master/doc/vimtex.txt"
[8]: https://github.com/lervag/vimtex "https://github.com/lervag/vimtex"
[9]: https://neovim.io/doc/user/api/ "https://neovim.io/doc/user/api/"
