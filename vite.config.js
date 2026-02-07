import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  base: '/internet_game_Build/',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        learn: resolve(__dirname, 'learn.html'),
        play: resolve(__dirname, 'play.html'),
      },
    },
  },
})
