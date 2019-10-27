# SONOS Volume Controller for M5StickC

Base is https://github.com/mjkillough/feather-sonos

[!https://raw.githubusercontent.com/masuidrive/sonos-controller-m5stickc/master/demo1.jpg]

# Install

```
export AMPY_PORT=/dev/tty.usbserial-XXXXXX
screen $AMPY_PORT 115200
```

Ctrl-C を複数回押して">>>"プロンプトを出す

```
ampy put xmltok.py /flash/xmltok.py

ampy put upnp.py /flash/upnp.py
ampy put sonos.py /flash/sonos.py
ampy put main.py /flash/main.py
ampy put discovery.py /flash/discovery.py
```

```
ampy get /flash/config.json config.json
```

ファイルの`"start": "flow"`を`"start": "app"`に変更

```
ampy put /flash/config.json config.json
```

screen \$AMPY_PORT 115200
Ctrl-C を複数回押して">>>"プロンプトを出す
