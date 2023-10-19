import uiautomator2 as u2
import time
import threading
import pandas as pd
import subprocess
import trace
import util
import math
import os


if __name__ == "__main__":
    # Load config
    config = util.load_config('config.yaml')
    trace_path = 'data/1/'
    # test_app_list = config['app_list']['app_list_30']
    test_app_list = ["com.UCMobile"]
    # test_app_list = ["me.ele", #饿了么
    # "com.wuba", #五八同城
    # "ctrip.android.view" #携程旅行
    # ]
    monkey_interval = config['base']['monkey_interval']
    stress_time_per_app = config['base']['stress_time_per_app']
    trace_interval = config['base']['trace_interval']
    duration = 20 # hours

    d = u2.connect('91822ff6')
    util.begin_watcher(d)
    d.shell('setprop debug.choreographer.skipwarning {}'.format(config['base']['jank_threshold'])) # set jank threshold 
    # d.shell('adb root')
    t_mute = threading.Thread(target=util.mute_phone,args=(d,),daemon=True)
    t_mute.start()

    # if d.shell("test -d /sdcard/tmp/apk && echo 'exist' || echo 'does not exist'").output == 'does not exist\n':
    #     # d.push('./apk/continue', '/sdcard/tmp/apk')
    #     subprocess.run(f'adb -s {d.serial} push ./apk/continue /sdcard/tmp/apk',shell=True)
    # apks = os.listdir('apk/continue')
    # for app in apks:
    #     d.shell("su -c 'pm install /data/tmp/apk/{}'".format(app))

    t_start = time.time()
    t_end = t_start + 3600 * duration
    t_tracing = util.T_tracing(d,trace_interval,3600*duration, trace.tracing_script_sagit)
    t_tracing.start()
    i = 0
    df_lt = pd.DataFrame(columns=test_app_list)
    while time.time() < t_end: 
        # trace.jank_reset(d, test_app_list)
        
        lt_list = []
        # app_list = []
        for package_name in test_app_list:
            lt, t, app_name = util.test_app(d, stress_time_per_app, package_name, monkey_interval)
            lt_list.append(lt)
            # app_list.append(app_name)
        try:
            # df_jank = trace.jank_collection(d, test_app_list)
            # pd.DataFrame(lt_list).transpose().to_csv(f'{trace_path}/lt{i}.csv', mode='a', index=False, header=False)
            df_lt.loc[len(df_lt.index)] = lt_list
            i += 1
            # df_jank.to_csv(f'{trace_path}/jank{i}.csv',sep=',',index=False,header=True)
        except Exception as e:
            print(str(e))
    df_tracing = t_tracing.get_result()
    df_tracing.to_csv(f'{trace_path}/tracing.csv',sep=',',index=False,header=True)
    df_lt.to_csv(f'{trace_path}/lt.csv',sep=',',index=False,header=True)
                
    # df_lt.transpose().to_csv(f'{trace_path}lt.csv',sep=',',index=False,header=True)            
    
