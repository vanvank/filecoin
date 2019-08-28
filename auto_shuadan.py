#!/usr/bin/env python3
import os
import subprocess
import re
import time


def import_file(file_path):
    hash = subprocess.check_output(['/home/xl/filecoin/go-filecoin','client','import',file_path])
    print(file_path)
    return hash.decode().strip()


def import_data(path):
    if os.path.isfile(path):
        hash = import_file(path)
        return hash
    elif os.path.isdir(path):
        data=os.listdir(path)
        hashs=[]
        for i in data:
            hash=import_data(os.path.join(path,i))
            hashs.append(hash)
        return hashs   


def get_go_filecoin_cmd_path():
    path=os.environ.get('PATH')
    home=re.search("(:?/.*filecoin):",path).group(1)
    cmd_path=os.path.join(home,"go-filecoin")
    return cmd_path


def propose_storage(hash, miner_id, ask_id, duration):
    t1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print("%s开始存%s" %(t1, hash))
    try:
        output = subprocess.check_output([get_go_filecoin_cmd_path(), 'client', 'propose-storage-deal', miner_id, hash, ask_id, duration])
        s = output.decode()
        print(s)
        DealID = re.search("\nDealID:(.*)",s).group(1).strip()
        cmd="./dealid_status.sh %s" %DealID
        with open("log.dealid", "a+") as f:
            subprocess.Popen(cmd,stdout=f,shell=True)
            t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            print("%s开始追踪DealID的状态 %s" %(t,DealID))
            print("半小时后刷下一单")
            time.sleep(1800)
    except Exception as e:
        print("存数据过程中发生了一些错误:%s, 跳过存下一个数据" %e)
        print("等1分钟再刷下一单")
        time.sleep(60)



def auto_shuadan(hashs, miner_id, ask_id, duration):
    if isinstance(hashs, str):
        #print("is str")
        propose_storage(hashs, miner_id, ask_id, duration)
    elif isinstance(hashs, list):
        #print("is dict")
        for hash in hashs:
            auto_shuadan(hash,miner_id, ask_id, duration)
    else:
        print("not str or dict")

def main():
    #### 1U 
    #miner_id='t2jxjdgvdevs7bl4dgzrxduqvzc4nuekdo2jfjdiq'
    #### xueyuan
    miner_id="t2vncxxefzpdfus7z5sxblqyugbfudltpgfbpcbli"
    ask_id=''
    duration='1440'
    #
    #path='/home/xl/sample_data/test.file'
    path='/tmp/300m.tar'
    hashs = import_data(path)
    print(hashs)
    auto_shuadan(hashs,miner_id, ask_id, duration)
    
def check_out():
    try:
        subprocess.check_output("exit 1", shell=True)
    except Exception as e:
        print(e)
        print("捕获到错误")



if __name__=="__main__":
    main()
    #check_out()
