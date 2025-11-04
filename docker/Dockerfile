#Uses postgres version 18 as our base image
FROM postgres:18
#Goes into the app directory(think of it like a cd terminal command)
WORKDIR /app
#Copy package (if needed)
COPY requirmentes.txt ./
#Install app dependencies
RUN npm install
#Copy the rest of the app into our container
COPY . .

ENV PORT=9000

EXPOSE 9000

#Run the app
CMD [ "npm","start" ]

