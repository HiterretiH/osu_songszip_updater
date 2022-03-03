from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from CurrentProgress import CurrentProgress
from threading import Thread


class DriveApi:
    def __init__(self, credentials_file: str):
        credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self._service = build("drive", "v3", credentials=credentials)

    def update_file(self, file_id: str, filename: str) -> CurrentProgress:
        progress = CurrentProgress()
        Thread(target=self.__update_file_thread, args=(file_id, filename, progress)).start()
        return progress

    def __update_file_thread(self, file_id: str, filename: str, progress: CurrentProgress):
        try:
            media = MediaFileUpload(filename, resumable=True)
            request = self._service.files().update(fileId=file_id, media_body=media)
            response = None
            while response is None:
                status, response = request.next_chunk()
                if status:
                    progress.set_progress(status.progress())
        finally:
            progress.set_progress(1)

    def remove_old_revisions(self, file_id):
        for revision in self.revisions_list(file_id)["revisions"][:-1]:
            self.revisions_delete(file_id, revision["id"])

    def revisions_list(self, file_id: str):
        return self._service.revisions().list(fileId=file_id).execute()

    def revisions_delete(self, file_id: str, revision_id: str):
        return self._service.revisions().delete(fileId=file_id, revisionId=revision_id).execute()
