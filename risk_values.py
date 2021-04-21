"""In memory handling of Risk assessments """

import os, json

class LogInformation:

    def __init__(self, logs_dir):
        """load existing log files into memory"""
        with open('cached-data.json', 'r') as cached_data:
            data = cached_data.read()
            self._known_data = json.loads(data)
        self._logged_actions = []
        for file in os.listdir(logs_dir):
            file_path = os.path.join(logs_dir, file)
            if os.path.isfile(file_path):
                self._load_logged_actions(file_path)

    def logged_actions(self):
        return self._logged_actions

    def addLog(self, file_uploaded):
        self._load_logged_actions(file_uploaded)

    def _load_logged_actions(self, file_path):
        with open(file_path, 'r') as log_file:
            log_data = log_file.read()
            activities = json.loads(log_data)
            for activity in activities:
                self._logged_actions.append(activity)

    def is_user_known(self, username):
        known_users = self._known_data["known_users"]
        for user in known_users:
            if user == username:
                return True
        return False

    def is_client_known(self, client):
        known_clients = self._known_data["known_clients"]
        for known_client in known_clients:
            if client == known_client:
                return True
        return False

    def is_ip_known(self, ip):
        known_ips = self._known_data["known_ips"]
        for known_ip in known_ips:
            if ip == known_ip:
                return True
        return False

    def is_ip_internal(self, ip):
        internal_ips = self._known_data["internal_ips"]
        for internal_ip in internal_ips:
            if ip == internal_ip:
                return True
        return False
