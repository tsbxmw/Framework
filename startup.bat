@echo off
echo ===========================================================================
echo =      StartUp the AutoTest Framework                                     =
echo =      version 0.0.1 generate                                             =
echo =      visit websit : github.com/tsbxmw/Framework to get lastest version  =
echo =      python 2.7 is nessary to start up the framework                    =
echo =      * * * *                                                            =
echo ===========================================================================



if exist startupsystem.py ( 


echo ===========================================================================
echo =      Start Up now ...                                                   =
echo ===========================================================================

echo ===========================================================================
echo = install the paramiko                                                    =
pip install paramiko
echo ===========================================================================

python startupsystem.py

) else (

echo ===========================================================================
echo =      Sorry, can not find the startupsystem.py file, check please        =
echo ===========================================================================
)

