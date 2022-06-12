FROM nginx
WORKDIR /var/log/nginx/log
RUN ["/bin/bash", "-c", "while true; do echo "Bookboon test"; sleep 1; done"]