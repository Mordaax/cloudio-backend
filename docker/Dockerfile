FROM python:3.11-alpine

EXPOSE 8000

ENV WORKING_DIR /app

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR $WORKING_DIR

# Project files
COPY app $WORKING_DIR/app
COPY manage.py $WORKING_DIR/manage.py
COPY cloud $WORKING_DIR/cloud
COPY key.json $WORKING_DIR/key.json
COPY mysite $WORKING_DIR/mysite

# Run migrations, and load the database with fixtures
#RUN python manage.py migrate && python manage.py loaddata users posts comments

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]