# Lib and workdir
FROM python
WORKDIR .

# Copy requirements from root folder
COPY . .
COPY requirements.txt .

# Update pip and install all requirements
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Set environments and run tests
ENV ENV=prod
CMD python3 -m pytest -sv /tests/* --alluredir=test_results/