FROM node:16.16-alpine3.15 as build-stage
WORKDIR /app
COPY . .
ARG VUE_APP_BACKEND_HOST
RUN npm install
RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html
