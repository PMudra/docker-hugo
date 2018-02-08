FROM alpine:3.6

ENV HUGO_VERSION 0.26
ENV HUGO_SHA 67e4ba5ec2a02c8164b6846e30a17cc765b0165a5b183d5e480149baf54e1a50

RUN set -eux; \
        apk update; \
        apk add --no-cache --virtual .fetch-deps \
		    ca-certificates \
		    openssl; \
        wget -O hugo.tar.gz "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz"; \
        echo "${HUGO_SHA} *hugo.tar.gz" | sha256sum -c -; \
        tar -C /usr/local/bin -xf hugo.tar.gz hugo; \
        rm hugo.tar.gz; \
        apk del .fetch-deps; \
        hugo version

EXPOSE 1313

CMD ["/usr/local/bin/hugo"]
