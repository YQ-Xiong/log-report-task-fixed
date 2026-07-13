Analyze the Apache-style access log at /app/access.log and save a JSON report to /app/report.json.

Success criteria:
1. /app/report.json exists and contains a JSON object.
2. The JSON object has exactly these keys: total_requests, unique_ips, and top_path.
3. total_requests is 6 and unique_ips is 3.
4. top_path is "/index.html".
