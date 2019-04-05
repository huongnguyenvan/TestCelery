FROM python
COPY requirements.txt /webapp/requirements.txt
WORKDIR /webapp
RUN pip install -r requirements.txt
COPY . /webapp
EXPOSE 8000
