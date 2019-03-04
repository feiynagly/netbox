from __future__ import unicode_literals

# module rate choice
MODULE_RATE_CHOICES = [
    [1000, '1G'],
    [10000, '10G'],
    [155, '155M'],
    [40000, '40G']
]

# Module type choice
TYPE_SFP = 1
TYPE_XFP = 2
TYPE_GLC_T = 3
TYPE_POS = 4
TYPE_X2 = 5
MODULE_TYPE_CHOICE = [
    [TYPE_SFP, 'SFP'],
    [TYPE_GLC_T, 'GLC-T'],
    [TYPE_XFP, 'XFP'],
    [TYPE_POS, 'POS'],
    [TYPE_X2, 'X2']
]

REACH_SR = 5
REACH_LR = 10
REACH_ER = 40
REACH_ZR = 80
# Module reach distance choices
MODULE_REACH_CHOICE = [
    [5, 'SR'],
    [10, 'LR'],
    [40, 'ER'],
    [80, 'ZR'],
]

# Module status choices
STATUS_IN_USE = 1
STATUS_IDEL = 2
STATUS_ABANDMENT = 3
STATUS_BORROW = 4
MODULE_STATUS_CHOICE = [
    [STATUS_IN_USE, '在用'],
    [STATUS_IDEL, '空闲'],
    [STATUS_ABANDMENT, '报废'],
    [STATUS_BORROW, '借用']
]

# Bootstrap CSS classes for module statuses
STATUS_CLASSES = {
    0: 'warning',
    1: 'success',
    2: 'info',
    3: 'primary',
    4: 'danger',
    5: 'default',
}
