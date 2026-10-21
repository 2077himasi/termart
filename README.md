# termart 🎨

> 终端 ASCII 艺术生成器 —— 把图片变成彩色字符画，把文字染成彩虹，在终端里下一场《黑客帝国》同款矩阵雨。
> Terminal ASCII Art Generator: image → colored ASCII, text → rainbow, and a Matrix rain screensaver.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org)
[![Dependency](https://img.shields.io/badge/dependency-pillow-orange.svg)](https://python-pillow.org)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](#)

---

## ✨ 特性

- 🖼️ **图片转 ASCII**：任意图片 → 终端彩色字符画（24-bit 真彩色），也能导出纯文本。
- 🌈 **文字彩虹**：把任意文字染成逐字渐变的彩虹色，适合做标题 / 装逼输出。
- 🌧️ **矩阵雨**：纯终端实现的《黑客帝国》代码雨动画，白绿渐变拖尾。
- 🧩 **零外部服务**：纯本地运行，唯一依赖是 Pillow，装好即用。
- 🪶 **单文件**：核心逻辑全部在 `termart.py` 一个文件里，易读易改。

## 📦 安装

```bash
# 方式一：直接克隆使用（推荐，零构建）
git clone https://github.com/your-name/termart.git
cd termart
pip install -r requirements.txt

# 方式二：作为命令行工具安装
pip install .
```

## 🚀 快速开始

```bash
# 1) 图片转彩色 ASCII（直接看效果）
python3 termart.py image example_circle.png

# 2) 文字彩虹
python3 termart.py text "Hello, terminal!"

# 3) 矩阵雨（在真实终端里运行，Ctrl+C 退出）
python3 termart.py rain -d 15
```

## 🖼️ 图片转 ASCII 示例

下面是示例图（一张彩虹圆环）被渲染成纯文本字符画的效果：

```text
                   .^;>_[1|\//t/\\1}-<l"'                   
               ':<}\jucXYJCLLQQLLCJUXcur/1+I`               
            `![/ncULOmqdkhaaaooaaahkbpwOQJzuf1<"            
          ;?tuXCOqbhoooahkkbbbbbbbkhaoooakpZLYvj{!.         
        ;{rcJOqkooahbpqwmZO000000OOZmqpbkaoohpZCXn(i.       
      "}rcCZda*akdqmOQLCCCCCCCCCCCCCCLQ0ZwpbaoobmLXx(I      
     >tvUOdo*hbqm0LCCCCLLQQ000000QQQLCCCCL0ZqdhoobmCcj-'    
   .?rzLwh*abqZ0CCCLQQ0OOZZZOOOOZZZOO00QLCCCQZwdh*ap0Yn1^   
  .]xXQpookpm0CJCLQ0OZO0LUXcvvvvcXUCQOZO00QCCCQZqbo*bOUn(^  
  ?rXQpookqZQCCLQ0OZ0Cznf\){}[[}{)|fxcUQZZOQLCJLOwba*bOUn)' 
 !fcLqookqZQJCL0OZOJvj|}?+~++++++++-[(fuY0ZO0QCJLOwba*d0Xr- 
'(uJmh*hpmQJCL0OZQXx\}_~+-]}{111}[?_~+](jcLZO0QLJLZqkooqCvt:
!fzQp*abw0CCLQOZ0Xr|]~+?})|/tfftt\){]_~-)fcLZO0LCJQmdh*bOYr]
]rYOb*hpmQJCQ0ZZJn\[~+]{|tfft//ttft|1[_~?(rYOZOQLJLZqk*hmJn\
}nUZh*kpZLJLQOZOXr(-<-})/jt/\|||/tft({?~+1fcQZOQLCCOqboowCu/
{nUZh*kpZLJLQOZ0Xr(-~-}(/jt/\((|\tft|{?~+1fcQZOQLCCOqboowCvt
[xYOk*hpmQJCQ0ZOUn\[~+]1|tftt///tff\)[_<?(rX0ZOQLJLZqk*amJu\
>jzQp*abw0CCL0OZQzj(?~+]{(\tfffft/(1[_~_1fvCZO0QCJQmdh*kOYx[
`|uJmh*kpZQJCQ0OZQzr|[+~_?[{1)))1}]-+~?)fvCZZ0QLJLOqbooqLcfI
 >jzQpoobqZLJCQ0OZ0Uuf([_+~+____+++_]1/xXQZO0QLJCOwda*bOYx] 
  [xY0d*obqZLJCLQOZZQUcrt(1[]??][{)/juYLOZO0QCJLOwda*kZJu|^ 
  '{nY0dookpmQCCCQ0OOZOQJYcunxxnucXUL0ZZO0QLCCQZqba*kZJu\,  
   '}xXQqa*hdwZQCCCLQ00OZZZOO00OOOZZOO0QLCCCLOwpkoodOUu|,   
    ._jcCZboohdwZ0LCCCLLQQ00000000QQLLCCCCQOwpko*hwLzr}^    
      ;)xXLmkoohbpwZ0LLCCCCCCCCCCCCCCCL0OmqdhoohqQYu/>.     
       .i(nXCZdaoohkdqwmZO0QQQQQQ00OZwqdbhooabmQYu/+`       
         .i{rvUQmphaooahkbbddddddbbkhaooohdw0Jzx(~`         
            ,~)jvXJ0Zqdkhaooooooooaakbpm0CYcx\-;.           
               ^!?(fncXUJLQ00OO00QLCUXcuj\[>,.              
                   `:>-})\frrrrrrj/|{?<I^.                  
```

> 实际在终端里运行 `python3 termart.py image example_circle.png` 会显示**彩色**版本。

## 🎛️ 命令行参数

**`image <path>`** — 图片转 ASCII

| 参数 | 说明 | 默认 |
| --- | --- | --- |
| `-w, --width` | 输出宽度（字符数） | `80` |
| `--no-color` | 输出纯文本（无颜色） | 关闭 |
| `--invert` | 反转明暗 | 关闭 |
| `-o, --output` | 保存到文件（自动去色） | 关闭 |

**`text <text>`** — 文字彩虹

| 参数 | 说明 | 默认 |
| --- | --- | --- |
| `-o, --output` | 保存到文件（自动去色） | 关闭 |

**`rain`** — 矩阵雨

| 参数 | 说明 | 默认 |
| --- | --- | --- |
| `-d, --duration` | 持续秒数 | `10` |
| `--speed` | 每帧间隔（秒），越小越快 | `0.06` |

## 🗺️ 路线图

- [ ] 支持 GIF / 视频逐帧转 ASCII 动画
- [ ] 增加更多字体与字符集预设（含中文大字）
- [ ] 导出为 `.svg` / `.png` 的彩色 ASCII 图
- [ ] 交互式 TUI 预览

## 🤝 贡献

欢迎提 Issue 和 PR！任何好玩的想法（新效果、新字符集、性能优化）都值得一试。

## 📄 许可证

[MIT](LICENSE) © termart contributors
