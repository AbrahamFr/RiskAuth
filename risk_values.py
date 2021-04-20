"""In memory handling of Risk assessments """

import os, json

class LogInformation:

  log_items = []

  def __init__(self, logs_dir):
      self._logged_actions = []
      print('logs_dir: ' + logs_dir)
      for file in os.listdir(logs_dir):
          print(file)
          file_path = os.path.join(logs_dir, file)
          if os.path.isfile(file_path):
              print(file_path)
              with open(file_path, 'r') as log_file:
                  log_data = log_file.read()
                  activities = json.loads(log_data)
                  for activity in activities:
                      self._logged_actions.append(activity)
      print(self._logged_actions)






