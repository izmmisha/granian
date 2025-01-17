# Granian benchmarks

Run at: 2023-03-13T21:11:56.281596

CPUs: 10

## RSGI response types

| Type | Total requests | RPS | avg latency | max latency |
| --- | --- | --- | --- | --- |
| bytes small (c80) | 1380440 | 91422 | 0.858ms | 4.418ms |
| str small (c80) | 1315281 | 87101 | 0.908ms | 5.16ms |
| bytes big (c160) | 17517 | 1163 | 136.72ms | 154.067ms |
| str big (c80) | 714000 | 47282 | 1.681ms | 6.789ms |


## Interfaces

| Request | Total requests | RPS | avg latency | max latency |
| --- | --- | --- | --- | --- |
| RSGI bytes (c80) | 1292625 | 85597 | 0.924ms | 5.615ms |
| RSGI str (c80) | 1323108 | 87618 | 0.902ms | 5.282ms |
| RSGI echo (c80) | 1133968 | 75097 | 1.043ms | 4.024ms |
| ASGI bytes (c640) | 1141818 | 76062 | 8.359ms | 26.572ms |
| ASGI str (c320) | 1144228 | 75747 | 4.192ms | 18.69ms |
| ASGI echo (c80) | 838143 | 55503 | 1.432ms | 5.551ms |
| WSGI bytes (c80) | 1305394 | 86445 | 0.918ms | 3.639ms |
| WSGI str (c80) | 1302313 | 86241 | 0.921ms | 8.204ms |
| WSGI echo (c80) | 1154695 | 76469 | 1.034ms | 7.109ms |


## vs 3rd parties

### async

| Mode | Total requests | RPS | avg latency | max latency |
| --- | --- | --- | --- | --- |
| Granian Asgi [GET] (c640) | 1143693 | 76163 | 8.347ms | 23.586ms |
| Granian Asgi [POST] (c80) | 829212 | 55269 | 1.44ms | 5.838ms |
| Granian Rsgi [GET] (c640) | 1282609 | 85435 | 7.443ms | 21.617ms |
| Granian Rsgi [POST] (c80) | 1138345 | 75882 | 1.043ms | 14.146ms |
| Uvicorn H11 [GET] (c160) | 225901 | 14992 | 10.653ms | 28.73ms |
| Uvicorn H11 [POST] (c160) | 196115 | 12999 | 12.281ms | 24.661ms |
| Uvicorn Httptools [GET] (c160) | 866771 | 57370 | 2.776ms | 13.478ms |
| Uvicorn Httptools [POST] (c160) | 780793 | 51954 | 3.068ms | 12.092ms |
| Hypercorn [GET] (c160) | 148668 | 9892 | 16.144ms | 34.448ms |
| Hypercorn [POST] (c160) | 132689 | 8818 | 18.1ms | 39.348ms |

### sync

| Mode | Total requests | RPS | avg latency | max latency |
| --- | --- | --- | --- | --- |
| Granian Wsgi [GET] (c80) | 1305116 | 86428 | 0.917ms | 3.644ms |
| Granian Wsgi [POST] (c80) | 1156180 | 76562 | 1.036ms | 3.218ms |
| Gunicorn Meinheld [GET] (c80) | 1321870 | 87533 | 0.912ms | 4.645ms |
| Gunicorn Meinheld [POST] (c80) | 1281454 | 84858 | 0.941ms | 5.217ms |



## Concurrency

### ASGI

| Concurrency | Total requests | RPS | avg latency | max latency |
| --- | --- | --- | --- | --- |
| P1 T1 wth (c320) | 1147172 | 75930 | 4.182ms | 18.771ms |
| P1 T1 rth (c160) | 699214 | 46290 | 3.431ms | 10.397ms |
| P1 T2 wth (c320) | 983613 | 65120 | 4.869ms | 16.905ms |
| P1 T2 rth (c640) | 696300 | 46351 | 13.715ms | 26.362ms |
| P1 T4 wth (c640) | 974840 | 64863 | 9.782ms | 39.747ms |
| P1 T4 rth (c320) | 711392 | 47367 | 6.723ms | 26.057ms |
| P2 T1 wth (c640) | 1950617 | 129933 | 4.839ms | 21.086ms |
| P2 T1 rth (c80) | 1265946 | 83831 | 0.934ms | 4.203ms |
| P2 T2 wth (c160) | 1458440 | 96571 | 1.661ms | 35.933ms |
| P2 T2 rth (c80) | 1152027 | 76287 | 1.069ms | 5.661ms |
| P2 T4 wth (c640) | 1449472 | 96015 | 6.582ms | 70.924ms |
| P2 T4 rth (c80) | 1216242 | 80544 | 0.986ms | 13.174ms |
| P4 T1 wth (c640) | 2204806 | 146403 | 3.895ms | 24.32ms |
| P4 T1 rth (c80) | 1485990 | 98407 | 1.187ms | 125.816ms |
| P4 T2 wth (c80) | 1344572 | 89330 | 1.948ms | 138.259ms |
| P4 T2 rth (c320) | 1471635 | 98059 | 3.196ms | 45.176ms |
| P4 T4 wth (c320) | 1467932 | 97350 | 4.07ms | 128.883ms |
| P4 T4 rth (c80) | 1443230 | 96090 | 0.853ms | 28.13ms |
| P5 T1 wth (c640) | 2184953 | 144917 | 4.105ms | 37.736ms |
| P5 T1 rth (c320) | 1649004 | 109884 | 2.827ms | 29.713ms |
| P5 T2 wth (c160) | 1503291 | 99864 | 9.719ms | 250.337ms |
| P5 T2 rth (c320) | 1750185 | 116623 | 2.657ms | 21.528ms |
| P5 T4 wth (c320) | 1390665 | 92060 | 6.132ms | 224.259ms |
| P5 T4 rth (c640) | 1967044 | 130440 | 4.263ms | 36.415ms |
| P10 T1 wth (c80) | 1365205 | 90413 | 12.546ms | 250.764ms |
| P10 T1 rth (c640) | 1841048 | 122191 | 6.321ms | 126.588ms |
| P10 T2 wth (c160) | 1261088 | 83612 | 12.026ms | 374.807ms |
| P10 T2 rth (c80) | 1445420 | 95738 | 9.352ms | 249.943ms |
| P10 T4 wth (c640) | 1449854 | 96234 | 8.594ms | 193.989ms |
| P10 T4 rth (c80) | 1403715 | 93088 | 2.669ms | 126.681ms |

### RSGI

| Concurrency | Total requests | RPS | avg latency | max latency |
| --- | --- | --- | --- | --- |
| P1 T1 wth (c640) | 1287374 | 85739 | 7.414ms | 23.882ms |
| P1 T1 rth (c320) | 914631 | 60551 | 5.253ms | 17.39ms |
| P1 T2 wth (c160) | 1410991 | 93425 | 1.686ms | 10.736ms |
| P1 T2 rth (c80) | 929603 | 61550 | 1.281ms | 3.81ms |
| P1 T4 wth (c640) | 1417314 | 94363 | 6.702ms | 30.847ms |
| P1 T4 rth (c80) | 1278644 | 84675 | 0.936ms | 4.853ms |
| P2 T1 wth (c320) | 2033699 | 135532 | 2.312ms | 16.011ms |
| P2 T1 rth (c80) | 1824917 | 120847 | 0.661ms | 5.068ms |
| P2 T2 wth (c640) | 2191097 | 145853 | 4.073ms | 20.777ms |
| P2 T2 rth (c80) | 1185000 | 78474 | 0.993ms | 3.734ms |
| P2 T4 wth (c160) | 1471612 | 97826 | 1.862ms | 63.56ms |
| P2 T4 rth (c80) | 1283394 | 84986 | 0.933ms | 35.727ms |
| P4 T1 wth (c640) | 2191051 | 145849 | 4.074ms | 24.943ms |
| P4 T1 rth (c160) | 1749368 | 116600 | 1.324ms | 8.669ms |
| P4 T2 wth (c640) | 2120426 | 140411 | 4.757ms | 103.048ms |
| P4 T2 rth (c320) | 1793723 | 119533 | 2.581ms | 13.976ms |
| P4 T4 wth (c160) | 1429695 | 94790 | 2.862ms | 135.922ms |
| P4 T4 rth (c640) | 2089238 | 138764 | 3.74ms | 46.745ms |
| P5 T1 wth (c640) | 2185071 | 145297 | 4.037ms | 25.892ms |
| P5 T1 rth (c320) | 1893449 | 126166 | 2.437ms | 24.548ms |
| P5 T2 wth (c80) | 1440375 | 95777 | 7.121ms | 249.917ms |
| P5 T2 rth (c640) | 2028350 | 134330 | 4.3ms | 47.116ms |
| P5 T4 wth (c160) | 1438866 | 95316 | 3.152ms | 149.033ms |
| P5 T4 rth (c640) | 2094585 | 138954 | 3.812ms | 56.567ms |
| P10 T1 wth (c640) | 2131500 | 141313 | 5.349ms | 130.972ms |
| P10 T1 rth (c640) | 1995780 | 132296 | 7.184ms | 142.457ms |
| P10 T2 wth (c160) | 1482121 | 98284 | 8.222ms | 349.899ms |
| P10 T2 rth (c640) | 2032240 | 134595 | 4.629ms | 159.899ms |
| P10 T4 wth (c320) | 1490046 | 98696 | 4.171ms | 129.504ms |
| P10 T4 rth (c640) | 2024347 | 134388 | 4.139ms | 116.435ms |

### WSGI

| Concurrency | Total requests | RPS | avg latency | max latency |
| --- | --- | --- | --- | --- |
| P1 T1 wth (c80) | 1301660 | 86198 | 0.92ms | 4.368ms |
| P1 T1 rth (c640) | 1232501 | 82105 | 72.477ms | 489.35ms |
| P1 T2 wth (c80) | 1387687 | 91895 | 0.879ms | 5.626ms |
| P1 T2 rth (c320) | 1107261 | 73301 | 4.775ms | 56.327ms |
| P1 T4 wth (c80) | 1367172 | 90511 | 1.038ms | 79.686ms |
| P1 T4 rth (c80) | 1099418 | 72805 | 1.099ms | 4.475ms |
| P2 T1 wth (c160) | 2063051 | 136598 | 1.134ms | 7.086ms |
| P2 T1 rth (c640) | 1996819 | 133022 | 21.145ms | 181.531ms |
| P2 T2 wth (c640) | 2196214 | 146148 | 4.058ms | 29.421ms |
| P2 T2 rth (c320) | 1746000 | 115588 | 2.748ms | 18.862ms |
| P2 T4 wth (c80) | 1398379 | 92591 | 4.68ms | 133.537ms |
| P2 T4 rth (c640) | 1448930 | 95894 | 6.663ms | 86.028ms |
| P4 T1 wth (c640) | 2254420 | 150149 | 3.993ms | 22.842ms |
| P4 T1 rth (c320) | 2270079 | 150288 | 1.947ms | 18.534ms |
| P4 T2 wth (c640) | 2222026 | 147723 | 4.63ms | 82.394ms |
| P4 T2 rth (c320) | 2218137 | 147405 | 1.962ms | 20.255ms |
| P4 T4 wth (c160) | 1472487 | 97477 | 12.661ms | 375.169ms |
| P4 T4 rth (c640) | 2224326 | 147178 | 4.096ms | 135.802ms |
| P5 T1 wth (c640) | 2257122 | 150172 | 3.975ms | 25.219ms |
| P5 T1 rth (c320) | 2256992 | 150273 | 1.786ms | 14.547ms |
| P5 T2 wth (c640) | 2182968 | 144629 | 4.712ms | 100.424ms |
| P5 T2 rth (c320) | 2274438 | 150830 | 2.148ms | 40.567ms |
| P5 T4 wth (c160) | 1458202 | 96565 | 7.694ms | 323.701ms |
| P5 T4 rth (c640) | 2253726 | 149274 | 3.955ms | 59.472ms |
| P10 T1 wth (c640) | 2252408 | 149914 | 4.948ms | 72.7ms |
| P10 T1 rth (c320) | 2292670 | 151786 | 2.035ms | 60.202ms |
| P10 T2 wth (c640) | 2030186 | 134716 | 5.095ms | 142.905ms |
| P10 T2 rth (c320) | 2301616 | 152501 | 2.613ms | 58.85ms |
| P10 T4 wth (c160) | 1454901 | 96594 | 3.393ms | 252.587ms |
| P10 T4 rth (c640) | 2284772 | 151472 | 4.475ms | 86.357ms |

