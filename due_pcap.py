#!/usr/bin/env python3

"""
  Keysight/DUE delay parameter change via input different .pcap
"""

import pyvisa as visa
import time
import argparse
import os
import logging

def connect(remote_host):
    rm = visa.ResourceManager()
    try:
        logging.debug(rm.list_resources())
        #E8267D 
        #cwsg=rm.open_resource( TCPIPO::192.168.10.51:: inst0:: INSTR')
        #cwsg.write(":FREQuency 3-78GHZ" )

        #S5040 connection build
        inst = rm.open_resource(f'TCPIP0::{remote_host}::SOCKET')
        inst.read_termination = '\n'
        inst.write_termination = '\n'
        logging.info(inst.query("*IDN?"))
        logging.info(inst.query("SERVer:VERsion?"))
        return inst
    except Exception as e:
        logging.error(f'{e}')
        raise e

def stop(inst):
    off_cnt = 0
    try:
        while True:
            inst.write("ORAN:REST:MOD0:PLAY:STOP")
            time.sleep(1)
            res = inst.query("ORAN:REST:MOD0:PLAY:STAT?")
            if res == "OFF":
                logging.info("STOP OFF, next")
                break
            else:
                logging.warning(f"STOP NOT OFF, continue({res})")
                off_cnt = off_cnt + 1
            if off_cnt == 10:
                logging.warning("STOP NOT OFF but force out")
                break
    except Exception as e:
        logging.error(f'{e}')
        raise e


def start(inst, pcap_path):
    try:
        #load pcap to the DUE server
        inst.write(f"ORAN:REST:MOD0:PCAP:LOAD {pcap_path}")
        logging.info("pcap loading done!")

        #start play the pcap file
        time.sleep(5)
        inst.write("ORAN:REST:MOD0:PLAY:STAR")

        logging.info("play the pcap done!")
                    
    except Exception as e:
        logging.error(f'{e}')

if __name__ == '__main__':
    logging.basicConfig(
            level=logging.INFO,
            format="[%(levelname)s] due-pcap: %(message)s")

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        'host', metavar='host', nargs='?', default='192.168.100.100::5060',
        help='the Rlogging.info server IP:Port of keysight DUE, e.g., 192.168.100.100::5060')
    parser.add_argument(
        'pcap', metavar='pcap', nargs='?',
        help='the name of pcap file w/o ./, e.g., FR1_100M_TM1-1_A1-5_273rb_4x4_for_325-200.pcap')

    args = parser.parse_args()

    remote_path = None
    if args.pcap:
        full_path = os.path.join('', args.pcap)
        if not os.path.exists(full_path):
            logging.error(f'{full_path} file not found')
            exit(-1)
        remote_path='C:\\DSP\\DPDK_Henry\\' + args.pcap

    inst = connect(args.host)
    stop(inst)
    if remote_path:
        start(inst, remote_path)
    inst.close()
