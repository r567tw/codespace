FROM alpine

WORKDIR /workspace

COPY templates ./templates
COPY playground ./playground

RUN apk update && apk upgrade 

RUN apk add supervisor
# can study from https://github.com/mlocati/docker-php-extension-installer
# ready for php/laravel env
RUN apk add php php-fpm php-pcntl php-json php-intl php-posix php-curl php-ctype php-phar php-iconv php-mbstring php-openssl php-pdo php-tokenizer php-opcache php-zlib php-dom php-xml php-xmlwriter php-fileinfo php-session

# copy composer file
COPY --from=composer /usr/bin/composer /usr/bin/composer
# composer global require laravel/installer

# supervisord : from-https://stackoverflow.com/questions/63608075/userwarning-supervisord-is-running-as-root-and-it-is-searching-for-its-configur
RUN echo user=root >>  /etc/supervisord.conf
CMD ["/usr/bin/supervisord","-n"]
