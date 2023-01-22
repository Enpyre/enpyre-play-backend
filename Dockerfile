FROM python:3.10-slim-bullseye

ARG ENVIRONMENT

USER root

RUN apt update -y && apt install -y vim curl libpq-dev gcc gnupg2 make

RUN curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | apt-key add - \
  && echo "deb https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list
RUN apt update -y && apt install -y doppler

RUN apt install --no-install-recommends -y ca-certificates locales locales-all \
  && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
  && update-ca-certificates \
  && echo 'America/Sao_Paulo' > /etc/timezone \
  && rm -rf /var/lib/apt/lists/*

RUN locale-gen pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt_br
ENV LC_ALL pt_BR.UTF-8

# Remove o delay do log
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY pyproject.toml .
COPY poetry.lock .
COPY install.sh .

RUN pip install --no-cache -U poetry && poetry config virtualenvs.create false
RUN ./install.sh

COPY . .

ENTRYPOINT ["doppler", "run", "--"]
CMD ["./start.sh"]
