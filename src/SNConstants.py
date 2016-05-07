#!/usr/bin/env python
# coding=utf-8
import base64

NKAccount = {
    'SHARE_KEY': base64.decodestring('emp4aW5saXN4MDE=')
}

SNAccount = {
    'SHARE_KEY': base64.decodestring('c2luZ2xlbmV0MDE=')
}

HNSNAccount = {
    'SHARE_KEY': base64.decodestring('aG5neDAx'),
    'SEC_KEY': base64.decodestring('MDAwYzI5MjcwNzEy'),
    'KEY_TABLE': base64.decodestring('YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY3ODkwWllYV1ZVVFNSUVBPTk1MS0pJSEdGRURDQkE6Xw==')
}

SNClient = {
    'CLIENT_VERSION': '1.2.22.36',
    'CLIENT_TYPE': base64.decodestring('c2luZ2xlTmV0')
}

HBDefault = {
    'DEFAULT_HB_DATA': base64.decodestring('bGx3bA=='),
    'SIG_SALT': base64.decodestring('TExXTFhBX1RQU0hBUkVTRUNSRVQ='),
    'SIG_SALT_MAC': base64.decodestring('TExXTFhB'),
    'ADAPTER_INFO': 'AMD PCNET Family PCI Ethernet Adapter - 数据包计划程序微型端口',
    'DEFAULT_EXPLORER': 'IE 6.0.2900.5512',
    'MEMORY_SIZE': 0x000001FF,
    'MAC_ADDRESS': '00-0C-29-F1-51-37',
    'CPU_INFO': 'Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz',
    'OS_LANG': 'Chinese-RPC',
    'OS_VERSION': 'Microsoft Windows XP Service Pack 3'
}
