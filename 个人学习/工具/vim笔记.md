---
title: Vim 笔记
date: 2025-9-19 22:32
category:
  - 个人学习
  - 工具
tags:
  - Vim
  - 编辑器
  - 教程
---

# vim note

算了没必要学这东西

vim 功能太多了还是键盘鼠标好用

---

In this note, I use neovim as the example.

## basic commands

In terminal, type `nvim` to open neovim.

```bash
$ nvim
```

to create a new file, type `nvim filename`.

```bash
$ nvim test.txt
```

After opening the file, we are in the editor.

### modes

there are three modles in Vim:

1. normal mode: for navigation and manipulation
2. insert mode: for inserting text
3. command mode: for executing commands

usually we start in normal mode.

#### normal mode

we can go through and use commends in normal mode

In normal mode, we can use keys to move the cursor

- <kbd>h</kbd>: move left
- <kbd>j</kbd>: move down
- <kbd>k</kbd>: move up
- <kbd>l</kbd>: move right

#### insert mode

We can edit text in insert mode.

there are several ways to enter insert mode

- <kbd>i</kbd>: insert
- <kbd>a</kbd>: append
- <kbd>o</kbd>: open a new line below
- <kbd>I</kbd>: insert before the line
- <kbd>A</kbd>: append at the end of the line
- <kbd>O</kbd>: open a new line above

and use <kbd>Esc</kbd> to exit insert mode and return to normal mode
