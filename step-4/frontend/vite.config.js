import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,
    port: 5173,
    proxy: {
      '/api': { target: 'http://backend:8000', changeOrigin: true },
      '/docs': { target: 'http://backend:8000', changeOrigin: true },
      '/openapi.json': { target: 'http://backend:8000', changeOrigin: true },
      '/redoc': { target: 'http://backend:8000', changeOrigin: true }
    }
  }
})
