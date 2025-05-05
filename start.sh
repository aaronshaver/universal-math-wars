#!/usr/bin/env bash
# Run Vite and FastAPI side‑by‑side; stop both on Ctrl‑C.

cd frontend
npm run dev &              # Vite → background
VITE_PID=$!

cd ../backend
uvicorn main:app --reload & # FastAPI → background
API_PID=$!

trap "kill $VITE_PID $API_PID" SIGINT SIGTERM
wait
