FROM pytorch/pytorch

COPY app.py /app.py

CMD python3 /app.py