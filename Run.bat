REM pytest -v -n=3 --html=Reports/report.html testcases/*  --browser chrome
REM pytest -v -n=3 --html=Reports/report.html testcases/test_login.py  --browser chrome
REM pytest -v -n=3 --html=Reports/report.html testcases/test_login.py  --browser firefox
pytest -v -m "sanity" --html=./Reports/report.html testcases/  --browser chrome
REM pytest -v -m "regression" --html=./Reports/report.html testcases/  --browser chrome
REM pytest -v -m "sanity or regression" --html=./Reports/report.html testcases/  --browser chrome
REM pytest -v -m "sanity and regression" --html=./Reports/report.html testcases/  --browser chrome