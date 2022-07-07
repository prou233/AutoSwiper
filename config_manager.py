import os
from configparser import ConfigParser

def change_conf(section,option,value):
    try:
        cp = ConfigParser()
        cp.read('config.ini',encoding='utf-8')
        cp.set(section, option, value)
        print('成功！')
    except:
        print('失败,请重试!')

def conf_page():
    os.system("cls")
    print('[config_manager][conf_page]正在读取配置文件...')
    cp = ConfigParser()
    cp.read('config.ini',encoding='utf-8')

    normal_mode = cp.get('modes', 'normal_mode')
    emulation_mode = cp.get('modes', 'emulation_mode')
    fast_mode = cp.get('modes', 'fast_mode')

    if normal_mode == 'True':
        mode = '正常模式'

    elif emulation_mode == 'True':
        mode = '仿真模式'

    elif fast_mode == 'True':
        mode = '快速模式'

    min_sleep_time = float(cp.get('config', 'min_sleep_time'))
    max_sleep_time = float(cp.get('config', 'max_sleep_time'))
    min_swipe_time = float(cp.get('config', 'min_swipe_time'))
    max_swipe_time = float(cp.get('config', 'max_swipe_time'))
    min_swipe_long = float(cp.get('config', 'min_swipe_long'))
    max_swipe_long = float(cp.get('config', 'max_swipe_long'))
    pause_probability = int(cp.get('config', 'pause_probability'))
    like_probability = int(cp.get('config', 'like_probability'))
    max_loop_count = int(cp.get('config', 'max_loop_count'))

    while True:
        os.system("cls")
        print('-----------------------------')
        print('配置文件：')
        print('模式：',mode)
        print('最小间隔时间：',min_sleep_time)
        print('最大间隔时间：',max_sleep_time)
        print('最小滑动时间：',min_swipe_time)
        print('最大滑动时间：',max_swipe_time)
        print('最小滑动距离：',min_swipe_long)
        print('最大滑动距离：',max_swipe_long)
        print('随机暂停概率：',pause_probability)
        print('随机点赞概率：',like_probability)
        print('最大循环次数：',max_loop_count)
        print('')
        print('-----------------------------')
        print('配置修改：')
        print('1    --------    修改最小间隔时间')
        print('2    --------    修改最大间隔时间')
        print('3    --------    修改最小滑动时间')
        print('4    --------    修改最大滑动时间')
        print('5    --------    修改最小滑动距离')
        print('6    --------    修改最大滑动距离')
        print('7    --------    修改随机暂停概率')
        print('8    --------    修改随机点赞概率')
        print('9    --------    修改最大循环次数')
        print('10   --------    修改托管模式')
        print('A    --------    返回首页')

        opition = input('请输入您需要的功能：')
        if opition == '1':
            var = int(input('请输入您要修改的值(原始值：%s)：'%min_sleep_time))
            change_conf('config','min_sleep_time',var)
        elif opition == '2':
            var = float(input('请输入您要修改的值(原始值：%s)：'%max_sleep_time))
            change_conf('config','max_sleep_time',var)
        elif opition == '3':
            var = float(input('请输入您要修改的值(原始值：%s)：'%min_swipe_time))
            change_conf('config','min_swipe_time',var)
        elif opition == '4':
            var = float(input('请输入您要修改的值(原始值：%s)：'%max_swipe_time))
            change_conf('config','max_swipe_time',var)
        elif opition == '5':
            var = float(input('请输入您要修改的值(原始值：%s)：'%min_swipe_long))
            change_conf('config','min_swipe_long',var)
        elif opition == '6':
            var = float(input('请输入您要修改的值(原始值：%s)：'%max_swipe_long))
            change_conf('config','max_swipe_long',var)
        elif opition == '7':
            var = float(input('请输入您要修改的值(原始值：%s)：'%pause_probability))
            change_conf('config','pause_probability',var)
        elif opition == '8':
            var = float(input('请输入您要修改的值(原始值：%s)：'%like_probability))
            change_conf('config','like_probability',var)
        elif opition == '9':
            var = float(input('请输入您要修改的值(原始值：%s)：'%max_loop_count))
            change_conf('config','max_loop_count',var)
        elif opition == '10':
            print('1：正常模式')
            print('2：仿真模式')
            print('3：快速模式')
            mode = str(input('请输入您需要的模式：'))
            change_conf('modes','normal_mode','False')
            change_conf('modes','emulation_mode','False')
            change_conf('modes','fast_mode','False')
            if mode == 1:
                change_conf('modes','normal_mode','True')
            elif mode == 2:
                change_conf('modes','emulation_mode','True')
            elif mode == 3:
                change_conf('modes','fast_mode','True')
        elif opition == 'A':
            break