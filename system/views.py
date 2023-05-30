from django.http import JsonResponse
from django.shortcuts import render
import psutil
import platform
import wmi
import pythoncom

# Create your views here.
def showDiskInfo() -> dict:
    disk_info={}
    #获取硬盘分区
    devs = psutil.disk_partitions()
    for dev in devs:
        G = 1024*1024*1024
        diskinfo = psutil.disk_usage(dev.device)
        #将字节转换成G
        # disk_info[dev.device.split(":")[0]]=('大小: %dG, 已使用: %dG, 未使用: %dG, 使用百分比:%d%%'%\
        #                         (diskinfo.total//G, diskinfo.used//G, diskinfo.free//G,diskinfo.percent))
        disk_info[dev.device.split(":")[0]]={"free":diskinfo.free//G, "total":diskinfo.total//G, "percent":diskinfo.percent}
    return disk_info

def get_cpu_percentage(request):
    cpu_percentage = dict(request.POST).get('cpu_percentage')[0]
    cpu_percentage=psutil.cpu_percent(interval=1)
    return JsonResponse({'cpu_percentage':cpu_percentage})
        
def hardware(request):
    cpu_name=""
    cpu_core=""
    cpu_speed=""
    cpu_percentage=0
    disk_info={}
    pythoncom.CoInitialize ()
    cpuinfo = wmi.WMI()
    for cpu in cpuinfo.Win32_Processor():
        cpu_name = cpu.Name # 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz
        # print("您的CPU已使用:%d%%" % cpu.LoadPercentage) # 17%
        cpu_percentage=cpu.LoadPercentage
        cpu_core=cpu.NumberOfCores # 4
        cpu_speed=format(cpu.MaxClockSpeed/1000,".2f") # 1690
    pythoncom.CoUninitialize ()
    disk_info=showDiskInfo()
    return render(request, "system/hardware.html",{"disk_info":disk_info,"cpu_name":cpu_name,"cpu_core":cpu_core,"cpu_speed":cpu_speed,"cpu_percentage":cpu_percentage})