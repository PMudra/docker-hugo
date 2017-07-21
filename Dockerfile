FROM alpine:3.6

ENV HUGO_VERSION 0.25.1
ENV HUGO_SHA fbf8ca850aaaaad331f5b40bbbe8e797115dab296a8486a53c0561f253ca7b00

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

ENTRYPOINT ["/usr/local/bin/hugo"]
