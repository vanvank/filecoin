#!/usr/bin/env python3
from useful_scripts import auto_shuadan, gen_files
import sys
# xueyuan
miner_id="t2vncxxefzpdfus7z5sxblqyugbfudltpgfbpcbli"
ask_id='1'
duration='1440'
path=sys.argv[1]
number=int(sys.argv[2])
gen_files.mass_gen(number,path)
hashs = auto_shuadan.import_data(path)
auto_shuadan.auto_shuadan(hashs,miner_id, ask_id, duration)
