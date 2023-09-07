#!/usr/bin/python3
"""backend endpoint"""

from datetime import datetime, timedelta

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'], strict_slashes=False)
def hgnx_info():
  """return json data"""
  slack_name = request.args.get('slack_name')
  track = request.args.get('track')
  
  if not slack_name or not track:
    return jsonify({'error': 'slack_name and track are required'}), 400
  
  current_utc_time = datetime.utcnow()
  tolerance = timedelta(minutes=2)
  
  lower_bound = current_utc_time - tolerance
  upper_bound = current_utc_time + tolerance
  
  if not (lower_bound <= current_utc_time <= upper_bound):
    return jsonify({'error': 'Current UTC time is not valid'}), 400
  
  current_day = current_utc_time.strftime("%A")
  utc_time = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")
  github_repo_url = "https://github.com/nabil2i/hgnx-stage1"
  github_file_url = "https://github.com/nabil2i/hgnx-stage1/blob/main/task1.py"
  status_code = 200

  response_data = {
    "slack_name": slack_name,
    "current_day": current_day,
    "utc_time": utc_time,
    "track": track,
    "github_file_url": github_file_url,
    "github_repo_url": github_repo_url,
    "status_code": status_code
  }
  
  return jsonify(response_data), 200

if __name__ == '__main__':
  host = '0.0.0.0'
  port = 5000
  app.run(host, port)
