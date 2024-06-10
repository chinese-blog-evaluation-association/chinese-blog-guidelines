# 贡献指南

## 讨论一个提案

在 [Issue](https://github.com/HowieHz/chinese-blog-guidelines/issues) 或 [Discussions](https://github.com/HowieHz/chinese-blog-guidelines/discussions) 提出即可。

## 提出一个新的提案

> 注意：提出一个新提案的前先进行充分讨论能减少被直接否决的风险。

一个提案由以下几部分构成

1. `README.md` 中的 `提案概要`
2. `./doc/template/` 文件夹下的解释文档
3. `./example/template/[提案号（字母要转换为小写）]/` 文件夹下的对应的示例文件（非强制）

### 提出一个新的 `CBGB` 提案

0. `fork` 此项目，并创建一个新的分支
1. 在 `README.md` 中添加`提案概要`，模仿前文格式添加对应超链接
2. 复制 `./doc/template/cbgb&&&.md` 到 `./doc/template/`，将文件名和文件内的 `&&&` 字符替换为对应的提案序号，作为此提案的解释文件
3. 将解释文件中`[概要]`字符替换为 `README.md` 中对应的`提案概要`
4. 将解释文件中的`解释`下的 `...` 替换为此提案的解释
5. 复制 `./example/template/cbgb&&&` 文件夹到 `./example/template/`，将文件夹名，文件名，以及文件内的 `&&&` 替换为对应的提案序号，作为此提案的示例文件
6. 完善示例文件内容
7. 提出 `pull request`
8. 等待审查以及合并

### 提出一个新的 `CBGG` 提案

0. `fork` 此项目，并创建一个新的分支
1. 在 `README.md` 中添加`提案概要`，模仿前文格式添加对应超链接
2. 复制 `./doc/template/cbgg&&&.md` 到 `./doc/template/`，将文件名和文件内的 `&&&` 字符替换为对应的提案序号，作为此提案的解释文件
3. 将解释文件中`[概要]`字符替换为 `README.md` 中对应的`提案概要`
4. 将解释文件中的`解释`下的 `...` 替换为此提案的解释
5. 复制 `./example/template/cbgg&&&/` 文件夹以及文件夹内的文件复制到 `./example/template/`，将文件夹名，文件名，以及文件内的 `&&&` 替换为对应的提案序号，作为此提案的示例文件
6. 完善示例文件内容
7. 提出 `pull request`
8. 等待审查以及合并

## 修订一个提案

1. `fork` 此项目，并创建一个新的分支
2. 修改你要修改的内容
3. 提出 `pull request`
4. 等待审查以及合并
