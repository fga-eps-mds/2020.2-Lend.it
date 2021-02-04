THIS_DIR := $(CURDIR)
PORT := 3000:3000
DOCSIFY := docsify serve 

create:
	sudo docker build -t documentation .

run:
	sudo docker run --rm -v "${THIS_DIR}":/usr/app -p ${PORT} documentation ${DOCSIFY}

start-docker:
	systemctl start docker