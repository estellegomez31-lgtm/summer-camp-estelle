<script setup>
import { useRoute, useRouter } from 'vue-router'
import { isLogged, getMe, logout as apiLogout } from './api.js'

const route = useRoute()
const router = useRouter()

function logout() { apiLogout(); router.push('/login') }
</script>

<template>
  <div class="phone">
    <header class="appbar" v-if="isLogged() && route.meta.nav">
      <div class="brand">
  <svg class="brand-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M3 11L12 3L21 11" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M5 9.5V20C5 20.5523 5.44772 21 6 21H9C9.55228 21 10 20.5523 10 20V15C10 14.4477 10.4477 14 11 14H13C13.5523 14 14 14.4477 14 15V20C14 20.5523 14.4477 21 15 21H18C18.5523 21 19 20.5523 19 20V9.5"
          stroke="#7DD3FC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  FamilyTask
</div>
      <button class="link" @click="logout">Quitter</button>
    </header>

    <main class="screen"><router-view /></main>

    <nav class="tabbar" v-if="isLogged() && route.meta.nav">
      <router-link to="/taches" class="tab"><span class="ico">✅</span>Tâches</router-link>
      <router-link to="/assistant" class="tab"><span class="ico">✨</span>Assistant</router-link>
      <router-link v-if="getMe() && getMe().is_admin" to="/famille" class="tab"><span class="ico">👨‍👩‍👧</span>Famille</router-link>
    </nav>
  </div>
</template>
