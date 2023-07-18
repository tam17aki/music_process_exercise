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
# librosaを用いた短時間フーリエ変換に基づく振幅スペクトルの表示

import librosa
import librosa.display
import matplotlib.pylab as plt
import numpy as np

# サンプルファイルの読み込み -> load関数
# librosa.exはlibrosa付属のサンプル音源
audio, sr = librosa.load(librosa.ex("trumpet"), sr=22050)

# 短時間フーリエ変換 ->戻り値は複素数
spec = librosa.stft(audio)

# 振幅スペクトログラムと位相スペクトログラムとに分解
mag, phase = librosa.magphase(spec)

# 振幅スペクトログラム表示
librosa.display.specshow(mag, cmap="magma", x_axis="time", y_axis="linear", sr=22050)
plt.colorbar()
plt.show()

# 振幅値をdB(対数)スケールに変換
# ref: dBを取る基準の大きさ -> np.maxを0dBとする
spec_dB = librosa.amplitude_to_db(mag, ref=np.max)

# dBスケールに変換した振幅スペクトログラム
librosa.display.specshow(spec_dB, x_axis="time", y_axis="linear", sr=22050)
plt.colorbar()
plt.show()
