#
# Copyright (C) 2015 MediaTek Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#

#add kernel source code path as head file search path
MTK_PLATFORM := $(subst ",,$(CONFIG_MTK_PLATFORM))
ccflags-y += -I$(srctree)/drivers/misc/mediatek/include
ccflags-y += -I$(srctree)/drivers/misc/mediatek/include/mt-plat/$(MTK_PLATFORM)/include
ccflags-y += -I$(srctree)/drivers/misc/mediatek/include/mt-plat
ccflags-y += -I$(srctree)/drivers/misc/mediatek/base/power/$(MTK_PLATFORM)
ccflags-y += -I$(srctree)/drivers/misc/mediatek/base/power/include
#workaround for include mmc/card/queue.h and mmc/core/core.h
ccflags-y += -I$(srctree)/drivers
ifeq ($(CONFIG_MTK_PLATFORM), "mt6757")
ccflags-y += -I$(srctree)/drivers/mmc/host/mediatek/mt6757/$(MTK_PLATFORM)
endif
ifeq ($(CONFIG_MTK_PLATFORM), "mt6798")
ccflags-y += -I$(srctree)/drivers/mmc/host/mediatek/mt6798/$(MTK_PLATFORM)
endif
ifeq ($(CONFIG_MTK_PLATFORM), "kiboplus")
ccflags-y += -I$(srctree)/drivers/mmc/host/mediatek/mt6757/$(MTK_PLATFORM)
endif

obj-$(CONFIG_MMC_MTK_PRO) += msdc.o

msdc-y += sd.o
msdc-y += dbg.o
msdc-y += mtk_sd_misc.o
msdc-y += msdc_tune.o
msdc-y += msdc_partition.o
msdc-y += autok.o
msdc-y += $(MTK_PLATFORM)/msdc_cust.o
msdc-y += $(MTK_PLATFORM)/autok_dvfs.o

ifeq ($(CONFIG_FPGA_EARLY_PORTING),y)
msdc-y += $(MTK_PLATFORM)/msdc_fpga_io.o
endif

ifeq ($(CONFIG_MTK_EMMC_SUPPORT_OTP),y)
msdc-y += emmc_otp.o
endif
