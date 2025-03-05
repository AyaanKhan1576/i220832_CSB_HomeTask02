# Use the official Node.js 16 image as the base
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and yarn.lock before installing dependencies
COPY package.json yarn.lock ./

# Install dependencies using Yarn
RUN yarn install --frozen-lockfile

# Copy the rest of the application files
COPY . .

# Build the application
RUN yarn build

# Expose port 3000
EXPOSE 3000

# Run the application using Yarn
CMD ["yarn", "start"]
