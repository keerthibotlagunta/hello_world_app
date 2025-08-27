# Use official Node.js LTS image
FROM node:18

# Set working directory inside container
WORKDIR /usr/src/app

# Copy application code
COPY app.js .

# Expose port 8080 (since ECS expects 80 by default)
EXPOSE 8080

# Start the application
CMD ["node", "app.js"]

