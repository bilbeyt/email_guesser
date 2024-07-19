FROM node:20.11-alpine

COPY . /frontend
WORKDIR /frontend

RUN yarn install
RUN yarn build

RUN yarn lint
CMD yarn serve -s build
