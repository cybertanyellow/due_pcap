# Introduce

Remote control Keysight S5040 DUE via VISA protocal writen in Python

# HOW-TO

## Prequirement

Install [rye](https://github.com/mitsuhiko/rye) first, which is packages management and virtual environment.
```sh
curl -sSf https://rye-up.com/get | bash
```

!!And remember to enable REST service at Keysight DUE throught GUI

## Initialize

```sh
rye sync
rye shell
```

## start or stop

`./due_pcap.py -h` for help/usage information,

```sh
usage: due_pcap.py [-h] [host] [pcap]

Keysight/DUE delay parameter change via input different .pcap

positional arguments:
  host        the Rlogging.info server IP:Port of keysight DUE, e.g., 192.168.100.100::5060
  pcap        the name of pcap file w/o ./, e.g., FR1_100M_TM1-1_A1-5_273rb_4x4_for_325-200.pcap

options:
  -h, --help  show this help message and exit
```

`./due_pcap.py host` without [pcap] will stop DUE traffic

`./due_pcap.py host pcap` will restart DUE traffic with specific .pcap, e.g.,
```sh
> ./due_pcap.py 192.168.2.94::5060 FR1_100M_TM1-1_A1-5_273rbs_4x4_for_DUE.pcap
/home/yellow/keysight/.venv/lib/python3.12/site-packages/pyvisa_py/tcpip.py:408: UserWarning: TCPIP:instr resource discovery is limited to the default interface.Install psutil: pip install psutil if you want to scan all interfaces.
  warnings.warn(
/home/yellow/keysight/.venv/lib/python3.12/site-packages/pyvisa_py/tcpip.py:121: UserWarning: TCPIP::hislip resource discovery requires the zeroconf package to be installed... try 'pip install zeroconf'
  warnings.warn(
[INFO] due-pcap: Keysight Technologies,S5040A,MY62340188,2.4.10301.0
[INFO] due-pcap: 1.3.0.0
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF, continue(NOT PRESENT)
[WARNING] due-pcap: STOP NOT OFF but force out
[INFO] due-pcap: pcap loading done!
[INFO] due-pcap: play the pcap done!
```

# Reference

* [PyVISA: Control your instruments with Python](https://pyvisa.readthedocs.io/en/latest/)
* [Pure Python implementation of a VISA library.](https://pypi.org/project/PyVISA-py/)
* [Rye: An Experimental Package Management Solution for Python](https://github.com/mitsuhiko/rye)
