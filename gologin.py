

import random
import string
import os
def GPU():
    return random.choice(["ANGLE(NVIDIA GeForce GT 1030 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1060 6 GB Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce 8400 GS Direct3D11 vs_4_1 ps_4_1)",
            "ANGLE(NVIDIA GeForce RTX 2070 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Mobility Radeon HD 5000 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1050 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon(TM) Vega 8 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 970 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 3070 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 8670 D + R7 240 Dual Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(ATI Radeon 3100 Graphics(Microsoft Corporation WDDM 1.1) Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(Intel(R) HD Graphics 4600 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 770 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1080 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 520 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon R9 200 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1050 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 630 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon R7 200 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 440 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Radeon RX 580 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 8470 D Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 750 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon(TM) Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1070 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon RX 5700 XT Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 3000 Direct3D11 vs_4_1 ps_4_1)",
            "ANGLE(NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 530 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 750 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Radeon RX 570 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 500 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce 9500 GT(Microsoft Corporation - WDDM v1.1) Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(NVIDIA GeForce GTX 1650 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Radeon RX550 / 550 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) UHD Graphics 630 Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(AMD Radeon(TM) Vega 3 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce 9600 GT Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(Intel(R) HD Graphics 5500 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon(TM) R9 200 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 3050 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(NVIDIA GeForce RTX 3070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1060 3 GB Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics Family Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA NVS 310 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 760 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Microsoft Basic Render Driver Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(NVIDIA GeForce GTX 1080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 4000 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 610 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics Direct3D11 vs_4_1 ps_4_1)",
            "ANGLE(NVIDIA GeForce GTX 1660 Ti with Max - Q Design Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Radeon RX 5500 XT Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 620 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon RX 6900 XT Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 710 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Radeon(TM) RX 470 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) UHD Graphics 610 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 3080 Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(Intel(R) HD Graphics 510 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon(TM) RX Vega 11 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA Quadro FX 1700(Microsoft Corporation - WDDM v1.1) Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(NVIDIA GeForce GTX 650 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 2070 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 8210 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 6320 Graphics Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(NVIDIA GeForce GTX 550 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) Iris(R) Plus Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 610 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Mobile Intel(R) 4 Series Express Chipset Family Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(NVIDIA GeForce GTX 1650 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 730 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 6470 M Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 5450 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 7480 D Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce 8500 GT Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(NVIDIA GeForce GTX 960 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 720 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon R5 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 335 M Direct3D11 vs_4_1 ps_4_1)",
            "ANGLE(NVIDIA GeForce RTX 2060 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon(TM) Vega 6 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce 9800 GT Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(Radeon(TM) RX 570 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1660 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 760(192 - bit) Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) UHD Graphics 600 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 3050 Laptop GPU Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce G210 Direct3D11 vs_4_1 ps_4_1)",
            "ANGLE(NVIDIA GeForce RTX 3060 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1660 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 4600 Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(Intel(R) HD Graphics 620 Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(NVIDIA GeForce GTX 1060 5 GB Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 740 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 7700 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 745 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 2080 Super with Max - Q Design Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon R7 M260 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 2080 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce RTX 2080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Radeon RX 580 Series Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(ATI Radeon HD 5450 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 8650 G + HD 8600 M Dual Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon(TM) RX Vega 10 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce 9500 GT Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(ATI Radeon HD 2400 Pro Direct3D11 vs_4_0 ps_4_0)",
            "ANGLE(Intel(R) HD Graphics 4400 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(ATI Radeon HD 5770 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Intel(R) HD Graphics 4000 Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(AMD Radeon HD 6290 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 640 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 7500 / 7600 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Radeon(TM) RX 460 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 420 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon R7 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(ATI Radeon HD 4200 Direct3D11 vs_4_1 ps_4_1)",
            "ANGLE(ATI Radeon HD 4300 / 4500 Series Direct3D11 vs_4_1 ps_4_1)",
            "ANGLE(NVIDIA GeForce GTX 980 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon(TM) R9 390 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GT 740 M Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon RX 6600 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(Radeon RX 590 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(AMD Radeon HD 6800 Series Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE(NVIDIA GeForce GTX 1060 3 GB Direct3D9Ex vs_3_0 ps_3_0)",
            "ANGLE(ATI Mobility Radeon HD 4200 Series Direct3D11 vs_4_1 ps_4_1)",
            "NVIDIA GeForce GT 1030 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1060 6 GB Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce 8400 GS Direct3D11 vs_4_1 ps_4_1)",
            "NVIDIA GeForce RTX 2070 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 3050 Laptop GPU / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1050 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 970 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 2060 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1050 Ti / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 3070 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1060 6 GB / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 760 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 770 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1080 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1650 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1050 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1070 / PCIe / SSE2 ",
            "NVIDIA GeForce GT 440 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 3060 Ti / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 980 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 750 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1070 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1660 Ti / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 750 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce 9500 GT(Microsoft Corporation - WDDM v1.1) Direct3D11 vs_4_0 ps_4_0)",
            "NVIDIA GeForce GTX 1650 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce 9600 GT Direct3D11 vs_4_0 ps_4_0)",
            "NVIDIA GeForce RTX 3050 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 3070 Ti / PCIe / SSE2 ",
            "NVIDIA GeForce GT 740 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1050 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 750 Ti / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 3070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1060 3 GB Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA NVS 310 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 760 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1080 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1080 Ti / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1660 Ti with Max - Q Design Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1660 SUPER / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 660 / PCIe / SSE2 ",
            "NVIDIA GeForce GT 710 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 3080 Direct3D9Ex vs_3_0 ps_3_0)",
            "NVIDIA Quadro FX 1700(Microsoft Corporation - WDDM v1.1) Direct3D11 vs_4_0 ps_4_0)",
            "NVIDIA GeForce GTX 650 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 2070 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 550 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1060 / PCIe / SSE2 ",
            "NVIDIA GeForce GT 610 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1650 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GT 730 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce 8500 GT Direct3D9Ex vs_3_0 ps_3_0)",
            "NVIDIA GeForce GTX 960 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1070 Ti / PCIe / SSE2 ",
            "NVIDIA GeForce GT 720 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GT 335 M Direct3D11 vs_4_1 ps_4_1)",
            "NVIDIA GeForce RTX 2060 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce 9800 GT Direct3D11 vs_4_0 ps_4_0)",
            "NVIDIA GeForce GTX 1660 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 760(192 - bit) Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 2080 SUPER / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 3050 Laptop GPU Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce G210 Direct3D11 vs_4_1 ps_4_1)",
            "NVIDIA GeForce GTX 970 / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 3060 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 650 Ti BOOST / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1660 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 3050 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1060 5 GB Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GT 740 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 745 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 3070 / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 2080 Super with Max - Q Design Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 2080 Ti / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 2060 SUPER / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 2080 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 2080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 960 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 1060 3 GB / PCIe / SSE2 ",
            "NVIDIA GeForce 9500 GT Direct3D11 vs_4_0 ps_4_0)",
            "NVIDIA GeForce RTX 2070 / PCIe / SSE2 ",
            "NVIDIA GeForce GT 1030 / PCIe / SSE2 ",
            "NVIDIA GeForce GTX 750 / PCIe / SSE2 ",
            "NVIDIA GeForce GT 640 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce RTX 3050 Ti Laptop GPU / PCIe / SSE2 ",
            "NVIDIA GeForce GT 420 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 980 Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GT 730 / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 2070 SUPER / PCIe / SSE2 ",
            "NVIDIA GeForce GT 740 M Direct3D11 vs_5_0 ps_5_0)",
            "NVIDIA GeForce GTX 1060 3 GB Direct3D9Ex vs_3_0 ps_3_0)",
            "NVIDIA GeForce GT 710 / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 3080 / PCIe / SSE2 ",
            "NVIDIA GeForce RTX 2080 / PCIe / SSE2 ",
            "GeForce GT 1030 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1060 6 GB Direct3D11 vs_5_0 ps_5_0)",
            "GeForce 8400 GS Direct3D11 vs_4_1 ps_4_1)",
            "GeForce RTX 2070 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 3050 Laptop GPU / PCIe / SSE2 ",
            "GeForce GTX 1050 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 970 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 2060 / PCIe / SSE2 ",
            "GeForce GTX 1050 Ti / PCIe / SSE2 ",
            "GeForce RTX 3070 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1060 6 GB / PCIe / SSE2 ",
            "GeForce GTX 760 / PCIe / SSE2 ",
            "GeForce GTX 770 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1080 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 960 / PCIe / SSE2 ",
            "GeForce GTX 1650 / PCIe / SSE2 ",
            "GeForce RTX 3070 / PCIe / SSE2 ",
            "GeForce GTX 1050 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1070 / PCIe / SSE2 ",
            "GeForce GT 440 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 3060 Ti / PCIe / SSE2 ",
            "GeForce GTX 980 / PCIe / SSE2 ",
            "GeForce GT 630 / PCIe / SSE2 ",
            "GeForce MX110 / PCIe / SSE2 ",
            "GeForce GTX 750 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1070 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1660 Ti / PCIe / SSE2 ",
            "GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 750 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce 9500 GT(Microsoft Corporation - WDDM v1.1) Direct3D11 vs_4_0 ps_4_0)",
            "GeForce GTX 1650 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce 9600 GT Direct3D11 vs_4_0 ps_4_0)",
            "GeForce RTX 3050 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GT 520 / PCIe / SSE2 ",
            "GeForce RTX 3070 Ti / PCIe / SSE2 ",
            "GeForce GT 740 / PCIe / SSE2 ",
            "GeForce GTX 1050 / PCIe / SSE2 ",
            "GeForce GTX 750 Ti / PCIe / SSE2 ",
            "GeForce RTX 3070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1060 3 GB Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 760 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1080 / PCIe / SSE2 ",
            "GeForce GTX 1080 Ti / PCIe / SSE2 ",
            "GeForce GTX 1660 Ti with Max - Q Design Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GT 530 / PCIe / SSE2 ",
            "GeForce GTX 1660 SUPER / PCIe / SSE2 ",
            "GeForce GTX 660 / PCIe / SSE2 ",
            "GeForce GT 710 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 560 Ti / PCIe / SSE2 ",
            "GeForce RTX 3080 Direct3D9Ex vs_3_0 ps_3_0)",
            "GeForce GTX 650 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 2070 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 550 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1060 / PCIe / SSE2 ",
            "GeForce GTX 650 / PCIe / SSE2 ",
            "GeForce GT 610 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1650 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GT 730 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce 8500 GT Direct3D9Ex vs_3_0 ps_3_0)",
            "GeForce GTX 960 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1070 Ti / PCIe / SSE2 ",
            "GeForce GT 720 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 2070 / PCIe / SSE2 ",
            "GeForce GTX 750 / PCIe / SSE2 ",
            "GeForce GT 335 M Direct3D11 vs_4_1 ps_4_1)",
            "GeForce RTX 2060 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "GeForce 9800 GT Direct3D11 vs_4_0 ps_4_0)",
            "GeForce GTX 550 Ti / PCIe / SSE2 ",
            "GeForce GTX 1660 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 760(192 - bit) Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GT 710 / PCIe / SSE2 ",
            "GeForce RTX 2080 SUPER / PCIe / SSE2 ",
            "GeForce GTX 1060 3 GB / PCIe / SSE2 ",
            "GeForce RTX 3050 Laptop GPU Direct3D11 vs_5_0 ps_5_0)",
            "GeForce G210 Direct3D11 vs_4_1 ps_4_1)",
            "GeForce GTX 970 / PCIe / SSE2 ",
            "GeForce RTX 3060 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 650 Ti BOOST / PCIe / SSE2 ",
            "GeForce GTX 1660 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 3050 / PCIe / SSE2 ",
            "GeForce 8400 GS / PCIe / SSE2 ",
            "GeForce 940 MX / PCIe / SSE2 ",
            "GeForce GTX 1060 5 GB Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 950 M / PCIe / SSE2 ",
            "GeForce GT 740 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 745 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 2080 Super with Max - Q Design Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 2080 Ti / PCIe / SSE2 ",
            "GeForce GT 620 / PCIe / SSE2 ",
            "GeForce RTX 2060 SUPER / PCIe / SSE2 ",
            "GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 2080 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "GeForce RTX 2080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "GeForce 9500 GT Direct3D11 vs_4_0 ps_4_0)",
            "GeForce GT 1030 / PCIe / SSE2 ",
            "GeForce GT 640 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GT 330 M / PCIe / SSE2 ",
            "GeForce RTX 3050 Ti Laptop GPU / PCIe / SSE2 ",
            "GeForce GT 420 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 980 Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GT 730 / PCIe / SSE2 ",
            "GeForce RTX 2070 SUPER / PCIe / SSE2 ",
            "GeForce GT 740 M Direct3D11 vs_5_0 ps_5_0)",
            "GeForce GTX 1060 3 GB Direct3D9Ex vs_3_0 ps_3_0)",
            "GeForce RTX 3080 / PCIe / SSE2 ",
            "GeForce RTX 2080 / PCIe / SSE2 ",
            "AMD Ryzen 5 3600 6 - Core Processor ",
            "AMD Ryzen 5 5600 H with Radeon Graphics ",
            "AMD Mobility Radeon HD 5000 Series Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 3500 U with Radeon Vega Mobile Gfx ",
            "AMD Radeon(TM) Vega 8 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 7 3800 X 8 - Core Processor ",
            "AMD A10 - 6700 APU with Radeon(tm) HD Graphics ",
            "AMD Radeon HD 8670 D + R7 240 Dual Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 7 5800 X 8 - Core Processor ",
            "AMD Ryzen 7 3700 X 8 - Core Processor ",
            "AMD Phenom(tm) 8600 B Triple - Core Processor ",
            "AMD Ryzen 9 5900 X 12 - Core Processor ",
            "AMD Ryzen 5 1600 Six - Core Processor ",
            "AMD Radeon R9 200 Series Direct3D11 vs_5_0 ps_5_0)",
            "AMD Radeon R7 200 Series Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 4600 G with Radeon Graphics ",
            "AMD Radeon(TM) Graphics ",
            "AMD Ryzen 5 5600 X 6 - Core Processor ",
            "AMD Radeon RX 5700 XT ",
            "AMD A4 PRO - 7300 B APU with Radeon HD Graphics ",
            "AMD Radeon HD 8470 D Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 3 3200 G with Radeon Vega Graphics ",
            "AMD Radeon(TM) Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD FX(tm) - 6300 Six - Core Processor ",
            "AMD Radeon RX 5700 XT Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 3600 X 6 - Core Processor ",
            "AMD Ryzen 5 3450 U with Radeon Vega Mobile Gfx ",
            "AMD Athlon 320 GE with Radeon Vega Graphics ",
            "AMD Ryzen 5 3500 X 6 - Core Processor ",
            "AMD Radeon R5 200 Series ",
            "AMD Ryzen 5 4600 H with Radeon Graphics ",
            "AMD 4700 S 8 - Core Processor Desktop Kit ",
            "AMD Athlon 3000 G with Radeon Vega Graphics ",
            "AMD Radeon(TM) Vega 3 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD Radeon(TM) R9 200 Series Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 2400 G with Radeon Vega Graphics ",
            "AMD Ryzen 5 2600 Six - Core Processor ",
            "AMD Ryzen 5 3500 6 - Core Processor ",
            "AMD Phenom(tm) II X4 960 T Processor ",
            "AMD A6 - 7480 Radeon R5, 8 Compute Cores 2 C + 6 G ",
            "AMD A10 - 5750 M APU with Radeon(tm) HD Graphics ",
            "AMD Radeon HD 8650 G ",
            "AMD FX(tm) - 8300 Eight - Core Processor ",
            "AMD Radeon RX 5600 XT ",
            "AMD Ryzen 7 2700 X Eight - Core Processor ",
            "AMD Athlon(tm) II X2 250 Processor ",
            "AMD Ryzen 7 1700 Eight - Core Processor ",
            "AMD FX(tm) - 8120 Eight - Core Processor ",
            "AMD Ryzen 7 4800 H with Radeon Graphics ",
            "AMD Radeon RX 6900 XT Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 5600 6 - Core Processor ",
            "AMD Athlon Silver 3050 U with Radeon Graphics ",
            "AMD Ryzen 7 3700 U with Radeon Vega Mobile Gfx ",
            "AMD Radeon(TM) RX Vega 10 Graphics ",
            "AMD Ryzen 7 3750 H with Radeon Vega Mobile Gfx ",
            "AMD Ryzen 3 3100 4 - Core Processor ",
            "AMD Radeon(TM) RX Vega 11 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD E1 - 2100 APU with Radeon(TM) HD Graphics ",
            "AMD Radeon HD 8210 Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 3400 G with Radeon Vega Graphics ",
            "AMD E - 300 APU with Radeon(tm) HD Graphics ",
            "AMD Radeon HD 6320 Graphics Direct3D9Ex vs_3_0 ps_3_0)",
            "AMD Ryzen 5 2500 U with Radeon Vega Mobile Gfx ",
            "AMD Radeon(TM) Vega 8 Graphics ",
            "AMD A8 - 5600 K APU with Radeon(tm) HD Graphics ",
            "AMD Ryzen 9 6900 HX with Radeon Graphics ",
            "AMD Ryzen 9 3900 XT 12 - Core Processor ",
            "AMD Radeon HD 6470 M Direct3D11 vs_5_0 ps_5_0)",
            "AMD Radeon HD 5450 Direct3D11 vs_5_0 ps_5_0)",
            "AMD A8 - 5500 APU with Radeon(tm) HD Graphics ",
            "AMD Ryzen 7 1800 X Eight - Core Processor ",
            "AMD A4 - 5300 APU with Radeon(tm) HD Graphics ",
            "AMD Radeon HD 7480 D Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 7 1700 X Eight - Core Processor ",
            "AMD A10 - 7850 K Radeon R7, 12 Compute Cores 4 C + 8 G ",
            "AMD PRO A6 - 8570 R5, 8 COMPUTE CORES 2 C + 6 G ",
            "AMD Radeon R5 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD Athlon(tm) X4 860 K Quad Core Processor ",
            "AMD Radeon(TM) RX Vega 11 Graphics ",
            "AMD Ryzen 3 3300 U with Radeon Vega Mobile Gfx ",
            "AMD Radeon(TM) Vega 6 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 3550 H with Radeon Vega Mobile Gfx ",
            "AMD Ryzen 3 PRO 2200 G with Radeon Vega Graphics ",
            "AMD FX(tm) - 8350 Eight - Core Processor ",
            "AMD A4 - 5300 B APU with Radeon(tm) HD Graphics ",
            "AMD Ryzen 7 5700 X 8 - Core Processor ",
            "AMD Ryzen 7 4700 U with Radeon Graphics ",
            "AMD 3020e with Radeon Graphics ",
            "AMD Ryzen 5 1500 X Quad - Core Processor ",
            "AMD FX - 8320E Eight - Core Processor ",
            "AMD A4 - 4000 APU with Radeon(tm) HD Graphics ",
            "AMD Radeon HD 7700 Series Direct3D11 vs_5_0 ps_5_0)",
            "AMD Phenom(tm) II X4 840 Processor ",
            "AMD Ryzen 7 5700 U with Radeon Graphics ",
            "AMD Ryzen 7 5700 G with Radeon Graphics ",
            "AMD Athlon(tm) II X4 640 Processor ",
            "AMD A4 - 9125 RADEON R3, 4 COMPUTE CORES 2 C + 2 G ",
            "AMD Radeon(TM) R3 Graphics ",
            "AMD Ryzen 5 5500 U with Radeon Graphics ",
            "AMD Radeon R7 M260 Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 9 3900 X 12 - Core Processor ",
            "AMD Ryzen 3 2200 G with Radeon Vega Graphics ",
            "AMD Phenom(tm) II X4 965 Processor ",
            "AMD Radeon HD 5800 Series ",
            "AMD Radeon HD 8650 G + HD 8600 M Dual Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD Radeon(TM) RX Vega 10 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD FX(tm) - 4300 Quad - Core Processor ",
            "AMD A6 - 7310 APU with AMD Radeon R4 Graphics ",
            "AMD Radeon(TM) R4 Graphics ",
            "AMD Ryzen 5 5600 G with Radeon Graphics ",
            "AMD Athlon Gold 3150 U with Radeon Graphics ",
            "AMD Ryzen 5 PRO 4650 U with Radeon Graphics ",
            "AMD Athlon(tm) II X4 620 Processor ",
            "AMD C - 60 APU with Radeon(tm) HD Graphics ",
            "AMD Radeon HD 6290 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 4500 U with Radeon Graphics ",
            "AMD Radeon HD 7500 / 7600 Series Direct3D11 vs_5_0 ps_5_0)",
            "AMD A10 - 7860 K Radeon R7, 12 Compute Cores 4 C + 8 G ",
            "AMD Ryzen 5 PRO 2400 G with Radeon Vega Graphics ",
            "AMD Ryzen 5 2600 X Six - Core Processor ",
            "AMD Athlon 200 GE with Radeon Vega Graphics ",
            "AMD A12 - 9720 P RADEON R7, 12 COMPUTE CORES 4 C + 8 G ",
            "AMD Radeon R7 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "AMD Athlon(tm) II X2 215 Processor ",
            "AMD Sempron(tm) 145 Processor ",
            "AMD Ryzen 3 3200 U with Radeon Vega Mobile Gfx ",
            "AMD Ryzen 9 5950 X 16 - Core Processor ",
            "AMD A8 - 7600 Radeon R7, 10 Compute Cores 4 C + 6 G ",
            "AMD Radeon(TM) R9 390 Series Direct3D11 vs_5_0 ps_5_0)",
            "AMD Radeon RX 6600 Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 7 2700 Eight - Core Processor ",
            "AMD Phenom(tm) II X4 955 Processor ",
            "AMD Radeon HD 6800 Series Direct3D11 vs_5_0 ps_5_0)",
            "AMD Ryzen 5 3600 XT 6 - Core Processor ",
            "AMD E1 - 2500 APU with Radeon(TM) HD Graphics ",
            "AMD Radeon HD 8200 / R3 Series ",
            "AMD Radeon R7 Graphics Direct3D11 vs_5_0 ps_5_0)"
        ])
def resolution():
    return random.choice('''360x640
    360x720
    360x740
    360x760
    360x770
    360x780
    360x800
    375x667
    375x812
    384x854
    390x844
    392x800
    393x786
    393x808
    393x830
    393x851
    393x873
    411x731
    412x1004
    412x732
    412x823
    412x846
    412x869
    412x883
    412x892
    412x906
    412x914
    412x915
    414x736
    414x896
    428x926
    768x1076
    884x1104
    810x1080
    768x1024
    834x1112
    820x1180
    1024x1366
    834x1194
    1280x900'''.splitlines()).strip()
class Gologin:
    def __init__(self) -> None:
        self.pathProfile = os.path.abspath("profile")
        self.preferences = open("Data\\Settings\\text.txt").read()
    def _createFolder(self, name):
        if not os.path.exists(self.pathProfile): os.mkdir(self.pathProfile)
        path = os.path.join(self.pathProfile, name)
        if not os.path.exists(path): os.mkdir(path)
        path = os.path.join(path, 'Default')
        if not os.path.exists(path): os.mkdir(path)
        with open(path+"\\Preferences", "w") as file:
            file.write(self.preferences)
    def proxy(self, txtProxy: str):
        proxyre = txtProxy.split('.')[0] + "." + txtProxy.split('.')[1]
        Proxy = txtProxy.split(':')[0] + ":" + txtProxy.split(':')[1]
        UserProxy = txtProxy.split(':')[2].strip()
        Passproxy = txtProxy.split(':')[3].strip()
        publicip = txtProxy.split(':')[0].strip()
    def _random_data(self, exits: str):
        randd = exits.splitlines()
        nFirstName = random.choice(randd)
        return nFirstName
    def _random_num(self, a):
        text = "0123456789"
        array = [random.choice(text) for _ in range(a)]
        return ''.join(array)
    def _random_string_and_num(self, a):
        characters = string.ascii_lowercase + "0123456789"
        result = ''.join(random.choice(characters) for _ in range(a))
        return result
    def _random_infotxt(self, exits):
        with open(exits, 'r') as file:
            lines = file.readlines()
            return random.choice(lines).strip()
    def change(self, data: str, origin, neww):
        return data.replace(origin, neww)

    def createProfile(self, nameProfile):
        self.preferences = self.change(self.preferences, "tb_name_profile_SSL", nameProfile)
        self.preferences = self.change(self.preferences, "tb_user_agen", self._random_infotxt(os.path.abspath("Data\\UA\\Chrome.txt")))
        self.preferences = self.change(self.preferences, "tb_platform", "Win32")
        # self.preferences = self.change(self.preferences, "tb_language", "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja-JP;q=0.6,ja;q=0.5,ko-KR;q=0.4,ko;q=0.3")
        self.preferences = self.change(self.preferences, "tb_language", "vi-VN")

        # dpdm_values = resolution().split('x')
        dpdm_values = ["500", "700"]
        self.preferences = self.change(self.preferences, "tb_do_phan_dai_man_hinhx", dpdm_values[0])
        self.preferences = self.preferences.replace("tb_do_phan_dai_man_hinhy", dpdm_values[1])

        self.preferences = self.change(self.preferences, "hardwareChanger", random.choice("2|4|8|16|32".split('|')).strip())
        tb_RAM = random.choice("1|2|4|8".split('|'))
        if int(tb_RAM.strip()) == 1:
            self.preferences = self.change(self.preferences, "tb_RAM", "4096")
        elif int(tb_RAM.strip()) == 2:
            self.preferences = self.change(self.preferences, "tb_RAM", "8192")
        elif int(tb_RAM.strip()) == 4:
            self.preferences = self.change(self.preferences, "tb_RAM", "16384")
        elif int(tb_RAM.strip()) == 8:
            self.preferences = self.change(self.preferences, "tb_RAM", "32768")

        self.preferences = self.change(self.preferences, "tb_video_inputs", str(random.randint(1,2)))
        self.preferences = self.change(self.preferences, "tb_audio_inputs", str(random.randint(0,2)))
        self.preferences = self.change(self.preferences, "tb_audio_outputs", str(random.randint(1,2)))
        self.preferences = self.change(self.preferences, "tb_webGL_vendor", "Google Inc. (Intel)")
        self.preferences = self.change(self.preferences, "tb_web_Renderer", GPU())

        self.preferences = self.change(self.preferences, "tb_web_mo_cung_trinh_duyet", "")


        num1 = f"{random.randint(0, 7)}.{self._random_num(11)}e-{random.randint(8, 9)}"
        self.preferences = self.change(self.preferences, "noiseValueChange", num1)

        # ------------------------------------ Fake canvasNoise ------------------------------------ \\
        num2 = f"{random.randint(0, 4)}.{self._random_num(8)}"
        self.preferences = self.change(self.preferences, "canvasNoiseChange", num2)

        # ------------------------------------ Fake RectsNoiceself.change ------------------------------------ \\
        num3 = f"{random.randint(2, 9)}.{self._random_num(4)}"
        self.preferences = self.change(self.preferences, "RectsNoiceChange", num3)

        # ------------------------------------ Fake uid ------------------------------------ \\
        num4 = self._random_string_and_num(58)
        self.preferences = self.change(self.preferences, "sqzdbzkff4zv8ev9mgm1a6m8xw8xucyeyqjo1bibdjph9cechdqkhocecu", num4)

        # ------------------------------------ Fake webglNoiseValue ------------------------------------ \\
        num5 = f"{random.randint(9, 20)}.{self._random_num(3)}"
        self.preferences = self.change(self.preferences, "20.089", num5)

        # ------------------------------------ Fake num_personal_suggestions ------------------------------------ \\
        num6 = str(random.randint(1, 10))
        self.preferences = self.change(self.preferences, "suggestions_change", num6)

        # ------------------------------------ Fake device_scale_factor ------------------------------------ \\
        num7 = f"{random.randint(1, 3)}.5"
        self.preferences = self.change(self.preferences, "scalefactorChange", num7)

        # ------------------------------------ Fake webglNoiseValue ------------------------------------ \\
        num8 = f"{random.randint(10, 99)}.{random.randint(0, 999)}"
        self.preferences = self.change(self.preferences, "webglNoiseValueChange", num8)

        # ------------------------------------ Fake PrevNavigationTime ------------------------------------ \\
        num9 = f"13315906{random.randint(0, 999999999)}"
        self.preferences = self.change(self.preferences, "PrevNavigationTimeChange", num9)

        # ------------------------------------ Fake announcement_notification_service_first_run_time ------------------------------------ \\
        num10 = f"13315898{random.randint(0, 999999999)}"
        self.change(self.preferences, "serviceruntimeChange", num10)



        random_choice = random.randint(1, 2)
        if random_choice == 1:
            num11 = str(random.randint(700, 999))
            self.preferences = self.preferences.replace("bottomChange", num11)

            num12 = str(random.randint(20, 800))
            self.preferences = self.preferences.replace("leftChange", num12)

            num18 = str(random.randint(1300, 1900))
            self.preferences = self.preferences.replace("rightChange", num18)

            num19 = str(random.randint(50, 200))
            self.preferences = self.preferences.replace("topChange", num19)
        elif random_choice == 2:
            num14 = str(random.randint(700, 999))
            self.preferences = self.preferences.replace("bottomChange", num14)

            num15 = "22"
            self.preferences = self.preferences.replace("leftChange", num15)

            num20 = str(random.randint(1300, 1900))
            self.preferences = self.preferences.replace("rightChange", num20)

            num21 = "60"
            self.preferences = self.preferences.replace("topChange", num21)
        self._createFolder(nameProfile)
