"""
============
Author:xufangshu
Time:2023/8/2 13:48
Project:run
============
"""
from pyqpanda import *

if __name__ == "__main__":
    qvm = CPUQVM()
    qvm.init_qvm()

    qvm.set_configure(29, 29)
    qubits = qvm.qAlloc_many(4)
    cbits = qvm.cAlloc_many(4)

    # 构建量子程序
    prog = QProg()
    prog << H(qubits[0]) << CNOT(qubits[0], qubits[1]) << Measure(qubits[0], cbits[0])

    # 量子程序运行1000次，并返回测量结果
    result = qvm.run_with_configuration(prog, cbits, 1000)

    # 打印量子态在量子程序多次运行结果中出现的次数
    print(result)
    qvm.finalize()
