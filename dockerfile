FROM ubuntu:20.04
WORKDIR /base
RUN ln -sf /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip cmake wget llvm
RUN apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev libgl1-mesa-glx

RUN pip3 install uvicorn fastapi pymysql pandas scikit-learn
RUN pip3 install python-multipart multipledispatch
RUN pip3 install opencv-python==4.5.4.60
RUN pip3 install requests
RUN pip3 install  numpy
RUN pip3 install python-dotenv
RUN pip3 install fastapi-mail
RUN pip3 install -U pydantic
# ENV XDG_RUNTIME_DIR=/base
# RUN chmod -R 777 /base
# ENV RUNLEVEL=3
CMD sh start_service.sh
