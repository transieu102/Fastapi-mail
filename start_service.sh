export PYTHONIOENCODING=UTF-8
export LANG=C.UTF-8
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/base
export PYTHONPATH=${PYTHONPATH}:/base
export PYTHONPATH=${PYTHONPATH}:/base/src
uvicorn main:app --port 80 --host 0.0.0.0 --workers 1
