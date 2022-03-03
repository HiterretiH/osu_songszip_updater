class CurrentProgress:
    def __init__(self):
        self.__progress = 0

    def set_progress(self, progress: float):
        self.__progress = progress

    def get_progress(self):
        return self.__progress


class CurrentProgressList(CurrentProgress):
    def __init__(self, counter: list[int]):
        super().__init__()
        if len(counter) < 2:
            counter.clear()
            counter.extend([0, 0])
        self._counter = counter

    def get_progress(self):
        if self._counter[1] == 0:
            return 0
        return self._counter[0] / self._counter[1]
