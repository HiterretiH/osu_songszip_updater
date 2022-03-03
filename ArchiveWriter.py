from threading import Thread
from Progress import ListProgress
import zipfile
import os


class ArchiveWriter:
    def create_archive(self, filename: str, path: str) -> ListProgress:
        counter = [0, 0]
        progress = ListProgress(counter)
        Thread(target=self.__create_archive_thread, args=(filename, path, counter)).start()

        return progress

    def __create_archive_thread(self, filename: str, path: str, counter: list[int]):
        with zipfile.ZipFile(file=filename, mode="w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as f:
            for root, dirs, files in os.walk(path):
                counter[1] += len(files)
            for root, dirs, files in os.walk(path):
                dir_path = os.path.relpath(root, path)
                for file in files:
                    f.write(os.path.join(root, file), os.path.join(dir_path, file))
                    counter[0] += 1
