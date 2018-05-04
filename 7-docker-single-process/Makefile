all:
	(cd miku; docker build . -t miku:latest)
	(cd fluentd; docker build . -t miku-fluentd:latest)

start-service:
	docker run --name miku-0 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-1 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-2 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-3 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-4 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-5 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-6 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-7 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-8 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest
	docker run --name miku-9 -d --rm --log-driver=fluentd --log-opt fluentd-address=localhost:24224 --log-opt tag=miku.log miku:latest

stop-service:
	docker stop miku-0
	docker stop miku-1
	docker stop miku-2
	docker stop miku-3
	docker stop miku-4
	docker stop miku-5
	docker stop miku-6
	docker stop miku-7
	docker stop miku-8
	docker stop miku-9
