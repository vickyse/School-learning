# Obj 1.2
ARG PHP_FPM_VER=8.2

# first stage
# Obj 2
FROM composer:latest AS builder

# Obj 1.1
LABEL version="1.0"
LABEL maintainer="Wei-TIng, Hong <s4752348@uq.edu.au>"

WORKDIR /app

# Obj 2
# Copy dependencies from conf in order to install them
COPY conf/composer.json /app/composer.json
# Install depemdencies with specified requierments
RUN composer install --no-dev --optimize-autoloader --no-interaction -vvv

# second stage
FROM php:${PHP_FPM_VER}-fpm-alpine
# install files related to Obj 3, Obj 4.2, Obj 4.3, Obj 6.1  on this base 
RUN apk add --no-cache \
        nginx \
        php-pdo \
        php-pdo_mysql \
        curl \
        supervisor


# Objective 4.1
COPY conf/nginx.conf /etc/nginx/nginx.conf

# deploy the supervisor to make sure entrypoint works smoothly
COPY conf/supervisord.conf /etc/supervisord.conf

# Obj 5
COPY src/ /var/www/html/
COPY --from=builder /app/vendor /var/www/vendor/

# Obj 6
# set health check with specified requirements
HEALTHCHECK --start-period=10s --interval=30s --timeout=10s --retries=3 \
        CMD curl -f http://localhost/ || exit 1

# Obj 7.1
EXPOSE 80

# Obj 7.2
VOLUME /var/www/html
# Obj 7.3
WORKDIR /var/www/html

# Obj 7.4
# Copy entrypoint script and set permissions
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]