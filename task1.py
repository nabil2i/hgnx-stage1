#!/usr/bin/python3
"""backend endpoint"""

from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'], strict_slashes=False)
def hgnx_info():
  """return json data"""
  slack_name = request.args.get('slack_name')
  track = request.args.get('track')
  
  if not slack_name or not track:
    return jsonify({'error': 'slack_name and track are required'}), 400
  
  current_time = datetime.utcnow();
  
  response_data = {
    "slack_name": slack_name,
    "current_day": current_time.strftime("%A"),
    "utc_time": current_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "track": track,
    "github_file_url": "https://github.com/nabil2i",
    "github_repo_url": "https://github.com/nabil2i",
    "status_code": 200
  }
  
  return jsonify(response_data), 200

if __name__ == '__main__':
  app.run()
