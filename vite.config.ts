import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // Expose to local network
    port: 3000, // Optional: set a specific port
    open: true, // Optional: open in browser automatically
  },
})
