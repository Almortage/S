FROM nikolaik/python-nodejs:python3.9-nodejs18
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN pip3 install --upgrade pip
#clonning repo 
RUN git clone https://github.com/jepthoniq/jepthon /root/jepthon
#working directory 
WORKDIR /root/jepthon
RUN apk add --update --no-cache p7zip
# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/jepthon/bin:$PATH"

CMD ["python3","-m","jepthon"]
