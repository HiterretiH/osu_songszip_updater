from google.oauth2 import service_account
from googleapiclient.discovery import build


class DriveApi:
    def __init__(self, credentials_file: str):
        credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self._service = build("drive", "v3", credentials=credentials)

    def files_update(self, file_id: str, filename: str):
        pass

    def revisions_list(self, file_id: str):
        return self._service.revisions().list(fileId=file_id).execute()

    def revisions_delete(self, file_id: str, revision_id: str):
        return self._service.revisions().delete(fileId=file_id, revisionId=revision_id).execute()
