@echo off
setlocal enabledelayedexpansion

set /a year=%~1
set /a "remainder=year %% 4"
if !remainder! neq 0 goto :common

set /a "remainder=year %% 100"
if !remainder! neq 0 goto :leap

set /a "remainder=year %% 400"
if !remainder! equ 0 goto :leap

:common
set result=0
goto :output

:leap
set result=1

:output

echo !result!
