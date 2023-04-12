import inspect
import sys
from types import FrameType
from typing import Any, Dict


class LVVTracer():
    def __init__(self, target_funtion ):
        self.target_fuction
        return self

    def __enter__(self) -> Any:
        sys.settrace(self.counter_LVV)
        return self

    def counter_LVV(self, frame: FrameType, event: str, arg: Any) -> dict[Any, Any]:
        count = {}
        cod=frame.f_code
        var_locals=frame.f_locals
            #if event == 'line':
                if cod.co_name = self.target_fuction:
                    for x, var in var_locals:
                        if var not in var_locals:
                            count[var] = 0
                        else:
                            count[var] += 1

                            return count


    def __exit__(self, exc_tp: Type, exc_value: BaseException,exc_traceback: TracebackType) -> Optional[bool]:
        # Note: we must return a non-True value here,
        # such that we re-raise all exceptions
       # if self.is_internal_error(exc_tp, exc_value, exc_traceback):
        #    return False  # internal error
        #else:
         return sys.settrace(None)

    def getLVVmap(self) -> dict:
        #print(f"{var}: {count} changes")
        return self.getLVVmap