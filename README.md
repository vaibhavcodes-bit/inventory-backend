# Inventory & Order Management System

## Overview

A full-stack Inventory & Order Management System built using FastAPI, React, PostgreSQL, Docker, and cloud deployment platforms.

The application allows users to:

* Manage Products
* Manage Customers
* Create and Manage Orders
* Track Inventory
* Automatically Reduce Stock when Orders are Created
* Prevent Orders when Stock is Insufficient

---

## Features

### Product Management

* Create Product
* View Products
* Update Product
* Delete Product
* Unique SKU Validation

### Customer Management

* Create Customer
* View Customers
* Update Customer
* Delete Customer
* Unique Email Validation

### Order Management

* Create Orders
* View Orders
* Update Orders
* Delete Orders
* Automatic Stock Reduction
* Inventory Validation
* Insufficient Stock Protection

---

## Tech Stack

### Frontend

* React
* Vite
* Ant Design
* Axios
* React Router

### Backend

* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

### Database

* PostgreSQL (Neon)

### Containerization

* Docker
* Docker Compose

### Deployment

* Vercel (Frontend)
* Render (Backend)

---

## Project Structure

Backend

inventory-backend/
├── app/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example

Frontend

inventory-frontend/
├── src/
├── public/
├── package.json
├── vite.config.js

---

## Environment Variables

Backend Example

DATABASE_URL=postgresql://username:password@host:5432/database
PORT=8000

Frontend Example

VITE_API_URL=https://inventory-backend-z1ks.onrender.com

---

## Local Setup

### Backend

Install dependencies

pip install -r requirements.txt

Run application

uvicorn app.main:app --reload

Backend URL

http://localhost:8000

API Docs

http://localhost:8000/docs

---

### Frontend

Install dependencies

npm install

Run application

npm run dev

Frontend URL

http://localhost:5173

---

## Docker Setup

Build Containers

docker-compose up --build

Stop Containers

docker-compose down

---

## Live Deployment

Frontend

https://inventory-frontend-lime-three.vercel.app/

Backend

https://inventory-backend-z1ks.onrender.com

API Documentation

https://inventory-backend-z1ks.onrender.com/docs

---

## GitHub Repositories

Frontend Repository

https://github.com/vaibhavcodes-bit/inventory-frontend

Backend Repository

https://github.com/vaibhavcodes-bit/inventory-backend

---

## Docker Image

Docker Hub Repository

https://hub.docker.com/r/vaibhavcodes/inventory-backend

---

## Business Rules Implemented

* Unique Product SKU Validation
* Unique Customer Email Validation
* Product Stock Validation
* Automatic Stock Reduction on Order Creation
* Prevent Order Creation when Stock is Insufficient
* Order Total Amount Calculation
* PostgreSQL Data Persistence

---

## Author

Vaibhav Pandey
