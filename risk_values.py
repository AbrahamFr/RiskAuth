"""In memory handling of Risk assessments """

import os, json

class LogInformation:

  def __init__(self, logs_dir):
      """load existing log files into memory"""
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
      print(self._logged_actions)



