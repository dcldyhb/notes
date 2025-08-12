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
- `<head></head>`：head 元素，该元素作为想在 HTML 页面中包含但不想向用户显示的内容的容器。包括想在搜索结果中显示的关键字和页面描述、用于设置页面样式的 CSS、字符集声明等等。
- `<meta charset="utf-8">`：该元素指明文档使用 UTF-8 字符编码，UTF-8 包括世界绝大多数书写语言的字符。它基本上可以处理任何文本内容。以它为编码还可以避免以后出现某些问题，没有理由再选用其他编码。
- `<meta name="viewport" content="width=device-width">`：视口元素可以确保页面以视口宽度进行渲染，避免移动端浏览器以比视口更宽的宽度渲染内容，导致内容缩小。
- `<title></title>`：<title> 元素。该元素设置页面的标题，显示在浏览器标签页上，也作为收藏网页的描述文字。
- `<body></body>`：<body> 元素。该元素包含期望让用户在访问页面时看到的全部内容，包括文本、图像、视频、游戏、可播放的音轨或其他内容。
