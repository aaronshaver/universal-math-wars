#!/usr/bin/env bash
# Run Vite and FastAPI side‑by‑side; stop both on Ctrl‑C.

# Vite
cd frontend
npm run dev &
VITE_PID=$!

# FastAPI
cd backend
poetry run uvicorn main:app --reload
API_PID=$!

trap "kill $VITE_PID $API_PID" SIGINT SIGTERM
wait