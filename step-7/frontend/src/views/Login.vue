<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { API, setToken, setMe } from '../api.js'

const router = useRouter()
const email = ref('')
const password = ref('')
const error = ref('')

async function connect() {
  error.value = ''
  if (!email.value.trim() || !password.value) { error.value = 'Email et mot de passe requis.'; return }
  const q = new URLSearchParams({ email: email.value.trim(), password: password.value })
  const r = await fetch(`${API}/api/login?${q}`, { method: 'POST' })
  if (!r.ok) { error.value = 'Email ou mot de passe incorrect.'; return }
  const data = await r.json()
  setToken(data.token); setMe(data)
  router.push('/taches')
}
</script>

<template>
<div class="hero">
  <div class="logo">
    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" width="34" height="34">
      <path d="M3 11L12 3L21 11" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M5 9.5V20C5 20.5523 5.44772 21 6 21H9C9.55228 21 10 20.5523 10 20V15C10 14.4477 10.4477 14 11 14H13C13.5523 14 14 14.4477 14 15V20C14 20.5523 14.4477 21 15 21H18C18.5523 21 19 20.5523 19 20V9.5"
      stroke="#1E3A8A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>

    </svg>
  </div>

  <h1>FamilyTask</h1>
  <p>Les tâches de toute la famille, au même endroit.</p>
</div>


    <div class="panel">
      <h2>Se connecter</h2>
      <label>Email</label>
      <input v-model="email" type="email" autocomplete="email" placeholder="ex : maman@durand.fr" @keyup.enter="connect" />
      <label>Mot de passe</label>
      <input v-model="password" type="password" autocomplete="current-password" placeholder="••••••" @keyup.enter="connect" />
      <button class="primary block" @click="connect">Se connecter</button>
      <p class="err" v-if="error">{{ error }}</p>
      <p class="switch">Pas encore de compte ? <router-link to="/signup">Créer ma famille</router-link></p>
    </div>
</template>
