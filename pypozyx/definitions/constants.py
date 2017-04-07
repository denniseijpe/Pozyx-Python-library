#!/usr/bin/env python
"""pypozyx.definitions.constants - contains all Pozyx constants, such as error definitions, delays, physical convertions."""

POZYX_ANCHOR = 0x00
POZYX_TAG = 0x20

MAX_BUF_SIZE = 100
MAX_SERIAL_SIZE = 28

POZYX_INT_MASK_ALL = 0x1F
POZYX_DELAY_POLLING = 0.002
POZYX_DELAY_LOCAL_WRITE = 0.001
POZYX_DELAY_LOCAL_FUNCTION = 0.005
POZYX_DELAY_REMOTE_WRITE = 0.005
POZYX_DELAY_REMOTE_FUNCTION = 0.01
POZYX_DELAY_INTERRUPT = 0.1
POZYX_DELAY_CALIBRATION = 1
POZYX_DELAY_MODE_CHANGE = 0.02
POZYX_DELAY_RANGING = 0.025
POZYX_DELAY_REMOTE_RANGING = 0.1
POZYX_DELAY_POSITIONING = 0.2
POZYX_DELAY_REMOTE_POSITIONING = 0.4
POZYX_DELAY_FLASH = 0.5
POZYX_FAILURE = 0x0
POZYX_SUCCESS = 0x1
POZYX_TIMEOUT = 0x8
POZYX_3D = 3
POZYX_2D = 2
POZYX_2_5D = 1
POZYX_INT_PIN0 = 0x0
POZYX_INT_PIN1 = 0x1

POZYX_LED_CTRL_LEDRX = 0x10
POZYX_LED_CTRL_LEDTX = 0x20
POZYX_LED_ON = True
POZYX_LED_OFF = False

POZYX_ANCHOR_MODE = 0
POZYX_TAG_MODE = 1

# The GPIO modes
POZYX_GPIO_DIGITAL_INPUT = 0
POZYX_GPIO_PUSHPULL = 1
POZYX_GPIO_OPENDRAIN = 1

# The GPIO pull resistor configuration
POZYX_GPIO_NOPULL = 0
POZYX_GPIO_PULLUP = 1
POZYX_GPIO_PULLDOWN = 2

# anchor selection modes
POZYX_ANCHOR_SEL_MANUAL = 0
POZYX_ANCHOR_SEL_AUTO = 1

# discovery options
POZYX_DISCOVERY_ANCHORS_ONLY = 0
POZYX_DISCOVERY_TAGS_ONLY = 1
POZYX_DISCOVERY_ALL_DEVICES = 2

# positioning algorithm options
POZYX_POS_ALG_UWB_ONLY = 0
POZYX_POS_ALG_LS = 2
POZYX_POS_ALG_TRACKING = 4

# positioning filters
FILTER_TYPE_NONE = 0
FILTER_TYPE_FIR = 1
FILTER_TYPE_IIR = 2
FILTER_TYPE_MOVINGAVERAGE = 3
FILTER_TYPE_MOVINGMEDIAN = 4
FILTER_TYPE_MOVINGMODUS = 5

# how to intercept pozyx events: by polling or by interrupts
MODE_POLLING = 0
MODE_INTERRUPT = 1

# Division factors for converting the raw register values to meaningful
# physical quantities
POZYX_POS_DIV_MM = 1.0
POZYX_PRESS_DIV_PA = 1000.0
POZYX_ACCEL_DIV_MG = 1.0
POZYX_GYRO_DIV_DPS = 16.0
POZYX_MAG_DIV_UT = 16.0
POZYX_EULER_DIV_DEG = 16.0
POZYX_QUAT_DIV = 16384.0
POZYX_TEMP_DIV_CELSIUS = 1.0

# error-code definitions
POZYX_ERROR_NONE = 0x00
POZYX_ERROR_I2C_WRITE = 0x01
POZYX_ERROR_I2C_CMDFULL = 0x02
POZYX_ERROR_ANCHOR_ADD = 0x03
POZYX_ERROR_COMM_QUEUE_FULL = 0x04
POZYX_ERROR_I2C_READ = 0x05
POZYX_ERROR_UWB_CONFIG = 0x06
POZYX_ERROR_OPERATION_QUEUE_FULL = 0x07
POZYX_ERROR_TDMA = 0xA0
POZYX_ERROR_STARTUP_BUSFAULT = 0x08
POZYX_ERROR_FLASH_INVALID = 0x09
POZYX_ERROR_NOT_ENOUGH_ANCHORS = 0x0A
POZYX_ERROR_DISCOVERY = 0X0B
POZYX_ERROR_CALIBRATION = 0x0C
POZYX_ERROR_FUNC_PARAM = 0x0D
POZYX_ERROR_ANCHOR_NOT_FOUND = 0x0E
POZYX_ERROR_GENERAL = 0xFF

# flash configuration types
POZYX_FLASH_REGS = 1
POZYX_FLASH_ANCHOR_IDS = 2
POZYX_FLASH_NETWORK = 3
POZYX_FLASH_ALL = 4

# possible pin configuration settings
POZYX_INT_CONFIG = 0x24
PIN_MODE_PUSHPULL = 0
PIN_MODE_OPENDRAIN = 1

PIN_ACTIVE_LOW = 0
PIN_ACTIVE_HIGH = 1

POZYX_ALL_CHANNELS = [1, 2, 3, 4, 5, 7]
POZYX_ALL_BITRATES = [0, 1, 2]
POZYX_ALL_PRFS = [1, 2]
POZYX_ALL_PLENS = [0x04, 0x14, 0x24, 0x34, 0x08, 0x18, 0x28, 0x0C]
