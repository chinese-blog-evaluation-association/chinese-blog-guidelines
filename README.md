# 中文博客倡议

共建更好的博客环境需要每位博主的参与！

本文链接：[在我的博客上阅读](https://howiehz.top/archives/chinese-blog-guidelines)、[在 GitHub 上阅读](https://github.com/HowieHz/chinese-blog-guidelines)  
推荐阅读：[中文博客圈列表](https://howiehz.top/archives/chinese-blogosphere-list)

> 最后更新时间 2024.6.6

- [中文博客倡议](#中文博客倡议)
  - [本倡议精神](#本倡议精神)
  - [不提倡的设计](#不提倡的设计)
  - [提倡的设计](#提倡的设计)
  - [设计编辑的建议](#设计编辑的建议)
  - [提倡的行为](#提倡的行为)
  - [将本文链接插入博客](#将本文链接插入博客)
    - [Markdown 格式版](#markdown-格式版)
    - [HTML 格式版](#html-格式版)
  - [Star History](#star-history)
  - [更新日志](#更新日志)

## 本倡议精神

- 提升访客阅读体验。

## 不提倡的设计

- [CBGB001](./doc/cbgb001.md) 自动播放多媒体资源。
- [CBGB002](./doc/cbgb002.md) 动态页面标题。
- [CBGB003](./doc/cbgb003.md) 页面加载时弹出提示框限制用户操作。
- [CBGB004](./doc/cbgb004.md) 过多的特效。
- [CBGB005](./doc/cbgb005.md) 检测到广告过滤程序后影响用户浏览内容。

## 提倡的设计

1. 整个站点应采用固定的一套排版样式（如在[中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines/)的基础上发展出一套自己的排版样式）
2. 在需要填写邮箱的地方（如评论区）进行邮箱强制验证，验证方式如：
   - 向邮箱发送一封带有验证码的邮件来验证。
   - 向邮箱发送一封带有验证链接的邮件，评需要到邮箱点击验证链接。

## 设计编辑的建议

1. 延迟跳转等设计要进行测试，避免出现被浏览器拦截的情况。
2. 在测试的时候给网站加入帧数显示，保证较差配置的设备也能稳定 60 fps 运行。

## 提倡的行为

1. 积极评论，即使无话可说也可以发送一些用于赞美的语句来鼓励认真写文的博主。

## 将本文链接插入博客

### Markdown 格式版

国内访问情况较通畅的地址

```markdown
[中文博客倡议](https://howiehz.top/archives/chinese-blog-guidelines)
```

GitHub 地址

```markdown
[中文博客倡议](https://github.com/HowieHz/chinese-blog-guidelines)
```

### HTML 格式版

国内访问情况较通畅的地址

```html
<a href="https://howiehz.top/archives/chinese-blog-guidelines" target="_blank" rel="noopener noreferrer" title="中文博客倡议书">中文博客倡议</a>
```

GitHub 地址

```html
<a href="https://github.com/HowieHz/chinese-blog-guidelines" target="_blank" rel="noopener noreferrer" title="中文博客倡议书">中文博客倡议</a>
```

## Star History

<a href="https://star-history.com/#HowieHz/chinese-blog-guidelines&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HowieHz/chinese-blog-guidelines&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HowieHz/chinese-blog-guidelines&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HowieHz/chinese-blog-guidelines&type=Date" />
 </picture>
</a>

## 更新日志

<details><summary>点我展开</summary>

2024.6.7

- 简化标题层次，如`设计-不提倡的设计` -> `不提倡的设计`
- 为`不提倡的设计`每项添加代号，起始为 `CBGB`(chinese-blog-guidelines bad design)，后添加三位数字，大小为 000-999
- 调整 `CBGB003` 简述
- - 调整前：在网站加载的时候启用 alert/confirm/prompt 弹窗阻塞用户操作
- - 调整后：页面加载时弹出提示框限制用户操作
- 为 `CBGB001`-`CBGB005` 添加解释文档和示例文件
- 添加文档目录

2024.6.7

- 在 [Allenyou](https://github.com/Allenyou1126)([github@Allenyou1126](https://github.com/Allenyou1126)) 的建议下在`设计-不提倡的设计`中添加有关防广告过滤器的说明

2024.6.6

- 在 [wildgun](http://wildgun.net/) 的建议下修改`设计-提倡的设计`中有关排版的倡议

2024.6.2

- 初版

</details>
