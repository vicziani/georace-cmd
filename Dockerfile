from python
WORKDIR /opt/georace
COPY app/* .
RUN pip install -Ur requirements.txt
ENTRYPOINT python georace.py