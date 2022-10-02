import tracemalloc
import time

class AlgoPerformance():
    def __init__(self):
        self._start = 0.0
        self._end = 0.0
        self._peak  = 0.0
        self._peak_units = " KB"

    def __scale_peak(self, peak):
        # if self._peak > 999: # MB
        #     self._peak_units = " MB"
        #     return peak / (1024 * 1024)
        return peak

    def __trace_mem(self):
        first_size, first_peak = tracemalloc.get_traced_memory()
        self._peak = self.__scale_peak(first_peak)
    
    def __timer_start(self):
        self._start = time.time()
    
    def __timer_stop(self):
        self._end= time.time()

    def __time_diff_ms(self) -> float:
        return (self._end - self._start) * 1000

    def start(self):
        tracemalloc.start()
        self.__timer_start()
        # print("Tracing Status : ", tracemalloc.is_tracing())

    def stop(self, time=True, mem=True):
        self.__timer_stop()
        self.__trace_mem()
        tracemalloc.stop()
        # print("Tracing Status : ", tracemalloc.is_tracing())
        if time : print(f"Time elapsed   : {self.__time_diff_ms()} ms")
        if mem:   print(f"Peak Memory    : {self._peak} {self._peak_units}")