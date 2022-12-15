#v100 sound camera ver1.0.0

from Maix import MIC_ARRAY as mic
from Maix import FPIOA
from fpioa_manager import fm
import lcd
import sensor
import gc

from Maix import utils      #heap mem使用量確認及び設定用
utils.gc_heap_size(2500000) #Heap mem山盛り設定　soundmap画像を480*480に引き伸ばし処理するため増量必要。

mic.init()
Fpioa = FPIOA()
LEDdir = (0,0,0)            #マイクアレイモジュールのLEDインジケーター表示。RGBの輝度を0-255で設定。まぶしいのでいらない。

#Maxi Bit用のピン設定。
Fpioa.set_function(23, fm.fpioa.I2S0_IN_D0);
Fpioa.set_function(22, fm.fpioa.I2S0_IN_D1);
Fpioa.set_function(21, fm.fpioa.I2S0_IN_D2);
Fpioa.set_function(20, fm.fpioa.I2S0_IN_D3);
Fpioa.set_function(19, fm.fpioa.I2S0_WS);
Fpioa.set_function(18, fm.fpioa.I2S0_SCLK);
Fpioa.set_function(17, fm.fpioa.GPIOHS28);
Fpioa.set_function(15, fm.fpioa.GPIOHS27);

while True:
    soundmap = mic.get_map()                        #マイクアレイから音源の推定位置を16*16pixelのgrayscaleで求める。
#    sumM = 0
#    sumMx = 0
#    sumMy = 0
    grayMap = []
    for mapx in range(16):
        grayLine = []
        for mapy in range(16):
#            sumM = sumM + soundmap.get_pixel(mapx,mapy)
#            sumMx = sumMx + (mapx * soundmap.get_pixel(mapx,mapy))
#            sumMy = sumMy + (mapy * soundmap.get_pixel(mapx,mapy))
            grayLine.append(soundmap.get_pixel(mapx,mapy))
#        print(grayLine)
        grayMap.append(grayLine)
#    if sumM > 0:
#        print(sumMx/sumM,sumMy/sumM)
    print(grayMap)
    sounddir = mic.get_dir(soundmap)                #soundmapから音源方向を求める？
    mic.set_led(sounddir,(LEDdir))                  #マイクアレイモジュールのLEDを光らせる。

mic.deinit()
