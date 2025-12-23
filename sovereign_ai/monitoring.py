import time
from metrics import record

def monitor_exec(score):
    record(score)
    print(f"[MONITOR] Execução registrada: score={score} time={time.time()}")
