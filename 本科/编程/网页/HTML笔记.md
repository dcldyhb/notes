# HTML 笔记

## 元素

1. 开始标签 （Opening tag）：`<p>`
2. 结束标签 （Closing tag）：`</p>`
3. 内容（Content）：元素的内容，可以是输入的文本本身
4. 元素（Element）：开始标签、结束标签与内容相结合，便是一个完整的元素
   - 元素可以有属性，包含的是不想在真正的内容中出现的和元素有关的额外信息，有值的属性应该包含
     1. 属性与元素名称（或上一个属性，如果元素有超过一个属性的话）之间的一个空格。
     2. 属性名，后接一个等号
     3. 一对引号包围的属性值

### 嵌套元素

元素可以嵌套在其他元素中。嵌套的元素必须正确地嵌套在开始标签和结束标签之间。

```html
<p>My cat is <strong>very</strong> cute.</p>
```

### 空元素

空元素没有内容，只有开始标签，没有结束标签

```html
<img src="images/firefox-icon.png" alt="My test image" />
```

### 案例分析

```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image" />
  </body>
</html>
```

- `<!DOCTYPE html>`：文档类型声明，告诉浏览器这是一个 HTML5 文档，现在用于保证文档能够正常读取
- `<html></html>`：HTML 元素，包含了整个文档的内容，有时也被称为根元素
- `<head></head>`：head 元素，包含了文档的元数据
