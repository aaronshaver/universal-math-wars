FROM node:20-slim

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the Vite port
EXPOSE 5173

# Command to run the Vite development server
# The --host flag is often needed to expose the server correctly in Docker
CMD ["npm", "run", "dev", "--", "--host"] 