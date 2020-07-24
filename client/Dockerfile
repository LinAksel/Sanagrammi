FROM node:14

WORKDIR /app
COPY package* /app/
RUN npm ci

COPY . .

RUN npm run build

CMD ["npm", "start"]