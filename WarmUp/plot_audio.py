#!/usr/bin/env python3

""" 音楽情報処理 n本ノック !! """

# MIT License

# Copyright (C) 2023 by Akira TAMAMORI

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Commentary:
# librosaを用いたオーディオデータの波形表示

import librosa
import librosa.display
import matplotlib.pylab as plt

# サンプルファイルの読み込み -> load関数
# Args:
#   path: 音声ファイルのパス情報
#   sr: サンプリング周波数 -> librosaは指定された値でリサンプリング
# Returns:
#   audio: 波形データ
#   sr: （リサンプリングされたあとの）サンプリング周波数

# librosa.exはlibrosa付属のサンプル音源
# see https://librosa.org/doc/latest/recordings.html
audio, sr = librosa.load(librosa.ex("trumpet"), sr=22050)

# audioの形状を確認 -> サンプル数を確認
print(audio.shape)  # (117601, 1) ->117601個のサンプル点が含まれる

# 波形表示 -> display.waveshow関数
plt.figure(figsize=(16, 4))  # 図のサイズ (横, 縦)
librosa.display.waveshow(y=audio, sr=22050)
plt.show()  # この1行が必要
