<script setup>
import { useRoute, useRouter } from 'vue-router'
import { isLogged, getMe, logout as apiLogout } from './api.js'

const route = useRoute()
const router = useRouter()

function logout() { apiLogout(); router.push('/login') }
</script>

<template>
  <div>
    <nav>
      <router-link to="/">Accueil</router-link>
      <router-link to="/tasks">Tâches</router-link>
      <router-link to="/members">Famille</router-link>
      <router-link to="/assistant">Assistant</router-link>
      <button @click="logout">Déconnexion</button>
    </nav>

    <router-view />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { logout as apiLogout } from './api.js'

const router = useRouter()
function logout() { apiLogout(); router.push('/login') }
</script>

<style>
nav {
  display: flex;
  gap: 15px;
  padding: 10px;
  background: #eee;
}
</style>
