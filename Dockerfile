FROM python

COPY trendingtweet /trend-bot/
COPY requirements.txt /tmp
RUN python3.7 -m pip install --user -r /tmp/requirements.txt

WORKDIR /trend-bot
CMD ["python3.7", "src/main.py", "--test"]



