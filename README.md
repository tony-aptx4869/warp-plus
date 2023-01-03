# warp-plus

------------------------

![Code Size](https://img.shields.io/github/languages/code-size/tony-aptx4869/warp-plus) ![Top Language](https://img.shields.io/github/languages/top/tony-aptx4869/warp-plus) ![GitHub stars](https://img.shields.io/github/stars/tony-aptx4869/warp-plus)

[![Run on Replit](https://replit.com/badge/github/tony-aptx4869/warp-plus)](https://replit.com/github/tony-aptx4869/warp-plus)


## About Warp+

WARP+ uses Cloudflare’s virtual private backbone, known as Argo, to achieve higher speeds and ensure your connection is encrypted across the long haul of the Internet. [Read more](https://blog.cloudflare.com/announcing-warp-plus/)

## About Script

A script for getting more and more GB on Warp+ (https://1.1.1.1)

## How to Use

Please copy your device ID(s), if there are more than one, copy each one, paste them into the `ids` array in the `main.py` file, save the modification, and run the `main.py` file with `Python`. Just like the command below.

```shell
python3 main.py
```

For those who use remote Linux servers, it may be inconvenient to continuously connect to the server through SSH or something else, you may use the `warp.service` file I provided to manage the script as a system service, including running, stopping, and viewing the status, and even set it to start automatically at boot. Please refer to the commands below.

```shell
cp warp.service /etc/systemd/system/warp.service
systemctl start   warp.service
systemctl status  warp.service
systemctl stop    warp.service
systemctl enable  warp.service
systemctl disable warp.service
```

For those who don't want or are inconvenient to run the script on their own computer and those who don't have a remote Linux server, you can run it on `Replit` by clicking the button at the top of this document or the one below.

[![Run on Replit](https://replit.com/badge/github/tony-aptx4869/warp-plus)](https://replit.com/github/tony-aptx4869/warp-plus)

## Python Environment Require

Python 3.8+

