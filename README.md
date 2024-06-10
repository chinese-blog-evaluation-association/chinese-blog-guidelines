# 中文博客倡议

共建更好的博客环境需要你的参与！

本文链接：[在我的博客上阅读](https://howiehz.top/archives/chinese-blog-guidelines)、[在 GitHub 上阅读](https://github.com/HowieHz/chinese-blog-guidelines)  
推荐阅读：[中文博客圈列表](https://howiehz.top/archives/chinese-blogosphere-list)-唯有超链接，能将互联网上一座座孤岛联系起来  

如想支持本项目，就为此项目点个⭐吧！
你指尖释放的善意，将指引我们继续前行。

> 最后更新时间 2024.6.10

## 本倡议精神

- 提升访客访问体验。

## 不提倡的设计

- [CBGB001](./doc/cbgb001.md) 自动播放多媒体资源。
- [CBGB002](./doc/cbgb002.md) 动态页面标题。
- [CBGB003](./doc/cbgb003.md) 页面加载时弹出提示框限制用户操作。
- [CBGB004](./doc/cbgb004.md) 过多的特效。
- [CBGB005](./doc/cbgb005.md) 检测到广告过滤程序后影响用户浏览内容。

## 提倡的设计

- [CBGG001](./doc/cbgg001.md) 整个站点应采用固定的一套排版样式。
- [CBGG002](./doc/cbgg002.md) 在填写邮箱，网站等信息时，为访客提供验证服务。

## 设计编辑的建议

1. 延迟跳转等设计要进行测试，避免出现被浏览器拦截的情况。
2. 在测试的时候给网站加入帧数显示，保证较差配置的设备也能稳定 60 fps 运行。

## 提倡的行为

1. 积极评论，即使无话可说也可以发送一些用于赞美的语句来鼓励认真写文的博主。

## 鸣谢

感谢本项目的[所有贡献者](https://github.com/HowieHz/chinese-blog-guidelines/graphs/contributors)，以及在各个平台为对本项目提出指导意见的各位。正是因为你们，才有了现在的`中文博客倡议`！

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
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HowieHz/chinese-blog-guidelines&type=Date&theme=dark" loading="lazy" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HowieHz/chinese-blog-guidelines&type=Date" loading="lazy" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HowieHz/chinese-blog-guidelines&type=Date" loading="lazy" />
 </picture>
</a>

## 更新日志

<details><summary>点我展开</summary>

2024.6.10

- 添加鸣谢部分
- 修改 README.md 引入部分

2024.6.9

- 去除文章开头的目录
- 添加构建程序：将 README.md，解释，示例合并到一个文件中。用于博客文章。
- 调整 `CBGG002` 解释文档（感谢 [Kegongteng](https://kegongteng.cn/)([github@gtxykn0504](https://github.com/gtxykn0504)) 在其中做出的贡献）

2024.6.8

- 简化标题层次，如`设计-不提倡的设计` -> `不提倡的设计`
- 为`不提倡的设计`每项添加代号，起始为 `CBGB`(chinese-blog-guidelines bad design)，后添加三位数字，大小为 000-999
- 为`提倡的设计`每项添加代号，起始为 `CBGG`(chinese-blog-guidelines good design)，后添加三位数字，大小为 000-999
- 调整 `CBGB003` 简述
- - 调整前：在网站加载的时候启用 alert/confirm/prompt 弹窗阻塞用户操作
- - 调整后：页面加载时弹出提示框限制用户操作
- 调整 `CBGG002` 简述（感谢 [Imken](https://imken.moe/)([github@immccn123](https://github.com/immccn123)), [呓语梦轩](https://blog.awaae001.top/)([github@awaae001](https://github.com/awaae001)) 对这个提案做出的贡献，以及 [Kegongteng](https://kegongteng.cn/)([github@gtxykn0504](https://github.com/gtxykn0504)) 提出最终的修改方案
- - 调整前：在需要填写邮箱的地方（如评论区）进行邮箱强制验证
- - 调整后：在填写邮箱，网站等信息时，为访客提供验证服务
- 为 `CBGB001`-`CBGB005` 添加解释文档和示例文件
- 添加文档目录

2024.6.7

- 在 [Allenyou](https://github.com/Allenyou1126)([github@Allenyou1126](https://github.com/Allenyou1126)) 的建议下在`设计-不提倡的设计`中添加有关防广告过滤器的说明

2024.6.6

- 在 [wildgun](http://wildgun.net/) 的建议下修改`设计-提倡的设计`中有关排版的倡议

2024.6.2

- 初版

</details>
