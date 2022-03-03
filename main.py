from DriveApi import DriveApi
from ArchiveWriter import ArchiveWriter
from time import sleep
from Progress import Progress


def progressbar(progress: Progress, bar_width: int, timeout: int):
    while progress.get_progress() < 1:
        sleep(timeout)
        length = int(progress.get_progress() * bar_width)
        print(f"{'#' * length}{'_' * (bar_width - length)} {int(progress.get_progress() * 100)}%", end="")
    print(f"{'#' * bar_width} 100%")


def main():
    pass

if __name__ == '__main__':
    main()
