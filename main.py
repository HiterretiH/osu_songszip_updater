from DriveApi import DriveApi
from ArchiveWriter import ArchiveWriter
from time import sleep
from Progress import Progress
import config


def draw_progressbar(progress: Progress, bar_width: int, timeout: int):
    while progress.get_progress() < 1:
        sleep(timeout)
        length = int(progress.get_progress() * bar_width)
        print(f"\r{'#' * length}{'_' * (bar_width - length)} {int(progress.get_progress() * 100)}%", end="")
    print(f"\r{'#' * bar_width} 100%")


def main():
    drive_api = DriveApi(config.credentials_file)
    archive = ArchiveWriter()

    print("Creating archive:")
    progress = archive.create_archive(config.filename, config.path)
    draw_progressbar(progress, 30, 1)

    print("Uploading file to Google drive:")
    progress = drive_api.update_file(config.file_id, config.filename)
    draw_progressbar(progress, 30, 1)
    drive_api.remove_old_revisions(config.file_id)

    print("Done")


if __name__ == '__main__':
    main()
