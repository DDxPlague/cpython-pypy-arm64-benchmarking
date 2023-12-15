#!/bin/sh

set -u

exec gunicorn wsgi:app \
	--worker-class gevent \
	--bind "0.0.0.0:${HTTPPORT}" \
	--keep-alive "${KEEP_ALIVE}" \
	--graceful-timeout "${GRACEFUL_TIMEOUT}" \
	--worker-connections "${CONCURRENT_CONNECTIONS}" \
	--backlog "${LISTEN_SLOTS}"

	
