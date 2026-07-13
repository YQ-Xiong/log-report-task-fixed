# log-report-task-fixed

This repository contains a fixed TB2 Harbor task for parsing a small Apache-style access log and writing a JSON summary report.

The fixes align the task with Harbor expectations: the artifact path is consistent, the Docker image is pinned, the leaked reference solution is removed from the agent image, and the verifier checks the actual report values while writing `reward.txt` and `ctrf.json` under `/logs/verifier/`.
