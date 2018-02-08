FROM alpine:3.7

ENV HUGO_VERSION 0.36
ENV HUGO_SHA dc373a46487422f35ddedf4a4d3a490019d6aa4789db2bdf7475ef675bdfdff7

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
