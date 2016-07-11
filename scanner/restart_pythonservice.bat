@echo off

cd %~dp0
taskkill -F -T -FI "IMAGENAME eq pythonservice*"
echo "kill done!"
ping -n 2 127.1 > nul

python topmgr.py start
echo "start service done!"
pause