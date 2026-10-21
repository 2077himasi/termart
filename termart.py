#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
termart — 终端 ASCII 艺术生成器 🎨

三个开箱即用的小功能：
  • image  把任意图片转成彩色 ASCII 艺术（直接打印到终端）
  • text   把文字变成彩虹渐变大字
  • rain   在终端里下一场《黑客帝国》同款矩阵雨

零外部服务、纯本地、依赖只有一个 Pillow。
"""

import argparse
import colorsys
import os
import random
import shutil
import sys
import time

# 字符集：从暗到亮（亮度递增），用于把灰度映射到字符
CHARS = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def _hsv_to_rgb(h, s, v):
    """h in [0,360), s/v in [0,1] -> (r, g, b) 0-255"""
    r, g, b = colorsys.hsv_to_rgb(((h % 360) / 360.0), s, v)
    return int(r * 255), int(g * 255), int(b * 255)


def _ansi(r, g, b, ch):
    """给字符 ch 上 24-bit 真彩色前景"""
    return f"\033[38;2;{r};{g};{b}m{ch}\033[0m"


def image_to_ascii(path, width=80, colored=True, invert=False):
    """把图片转成 ASCII 艺术，可选彩色输出。"""
    from PIL import Image

    if not os.path.isfile(path):
        raise FileNotFoundError(f"找不到图片: {path}")

    img = Image.open(path).convert("RGB")
    w, h = img.size
    # 终端字符高度约为宽度的 2 倍，高度方向折半以修正视觉比例
    aspect = (h / w) / 2.0
    new_w = max(1, int(width))
    new_h = max(1, int(new_w * aspect))
    img = img.resize((new_w, new_h))
    px = img.load()

    out = []
    for y in range(new_h):
        line = ""
        for x in range(new_w):
            r, g, b = px[x, y]
            lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
            if invert:
                lum = 1.0 - lum
            ch = CHARS[min(len(CHARS) - 1, int(lum * (len(CHARS) - 1)))]
            if colored and ch != " ":
                line += _ansi(r, g, b, ch)
            else:
                line += ch
        out.append(line)
    return "\n".join(out)


def rainbow_text(text):
    """每个字符按 hue 渐变上色，输出彩虹文字。"""
    out = []
    for i, ch in enumerate(text):
        if ch == "\n":
            out.append("\n")
            continue
        r, g, b = _hsv_to_rgb(i * 18, 0.85, 1.0)
        out.append(_ansi(r, g, b, ch))
    return "".join(out)


def matrix_rain(duration=10.0, speed=0.06, trail=10):
    """终端矩阵雨动画，duration 秒后自动停止（Ctrl+C 可提前退出）。"""
    if not sys.stdout.isatty():
        print("(矩阵雨需要交互式终端才能演示，已跳过)")
        return

    glyphs = "アカサタナハマヤラワガザダバパ0123456789ABCDEF#$%&*+=<>/"
    h, w = shutil.get_terminal_size((24, 80))
    drops = [random.randint(-h, 0) for _ in range(w)]
    frame = 0

    def cell(x, y, t):
        c = glyphs[(x * 7 + y * 13 + frame * 3) % len(glyphs)]
        if t == 0:
            return f"\033[97m{c}"  # 头部：白色高亮
        g = 255 - int(190 * t / trail)
        return f"\033[38;2;0;{max(g, 30)};0m{c}"  # 尾部：渐暗的绿色

    try:
        while time.time() < time.time() + duration:
            buf = [[" "] * w for _ in range(h)]
            for x in range(w):
                head = drops[x]
                for t in range(trail):
                    y = head - t
                    if 0 <= y < h:
                        buf[y][x] = cell(x, y, t)
                drops[x] += 1
                if drops[x] - trail > h and random.random() > 0.95:
                    drops[x] = random.randint(-6, 0)
            sys.stdout.write("\033[2J\033[H")
            sys.stdout.write("\n".join("".join(row) for row in buf) + "\n")
            sys.stdout.flush()
            frame += 1
            time.sleep(speed)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[0m")


def _strip_ansi(s):
    import re
    return re.sub(r"\033\[[0-9;]*m", "", s)


def main():
    p = argparse.ArgumentParser(
        prog="termart",
        description="终端 ASCII 艺术生成器 🎨 (image / text / rain)",
    )
    sub = p.add_subparsers(dest="cmd")

    pi = sub.add_parser("image", help="图片转彩色 ASCII 艺术")
    pi.add_argument("path", help="图片路径")
    pi.add_argument("-w", "--width", type=int, default=80, help="输出宽度(字符)，默认 80")
    pi.add_argument("--no-color", action="store_true", help="输出纯文本(无颜色)")
    pi.add_argument("--invert", action="store_true", help="反转明暗")
    pi.add_argument("-o", "--output", help="保存到文件(自动去除颜色)")

    pt = sub.add_parser("text", help="文字彩虹渐变")
    pt.add_argument("text", help="要显示的文本，建议加引号")
    pt.add_argument("-o", "--output", help="保存到文件(自动去除颜色)")

    pr = sub.add_parser("rain", help="终端矩阵雨")
    pr.add_argument("-d", "--duration", type=float, default=10.0, help="持续秒数，默认 10")
    pr.add_argument("--speed", type=float, default=0.06, help="每帧间隔(秒)，越小越快")

    args = p.parse_args()

    if args.cmd == "image":
        art = image_to_ascii(args.path, args.width, not args.no_color, args.invert)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(_strip_ansi(art))
            print(f"已保存(纯文本) → {args.output}")
        else:
            print(art)
    elif args.cmd == "text":
        art = rainbow_text(args.text)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(_strip_ansi(art))
            print(f"已保存(纯文本) → {args.output}")
        else:
            print(art)
    elif args.cmd == "rain":
        matrix_rain(args.duration, args.speed)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
