FROM python:3.6-buster
RUN pip install pwn
COPY main.py /run/
CMD socat -T 5 -d -d tcp-l:10081,reuseaddr,fork,crlf EXEC:"python /run/main.py"