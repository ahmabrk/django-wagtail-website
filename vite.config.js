import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()],
  build: {
    manifest: true,
    outDir: 'static/dist',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        app: 'static/src/app.css'
      },
      output: {
        assetFileNames: 'assets/[name][extname]'
      }
    }
  }
})
