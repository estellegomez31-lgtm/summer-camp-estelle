<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { API, setToken, setMe } from '../api.js'

const router = useRouter()
const family = ref('')
const name = ref('')
const lien = ref('mère')
const email = ref('')
const password = ref('')
const error = ref('')
const LIENS = ['mère', 'père', 'fille', 'fils', 'frère', 'sœur', 'grand-mère', 'grand-père', 'oncle', 'tante']

async function submit() {
  error.value = ''
  if (!family.value.trim() || !name.value.trim() || !email.value.trim() || !password.value) {
    error.value = 'Remplis tous les champs.'; return
  }
  const q = new URLSearchParams({
    email: email.value.trim(), password: password.value,
    name: name.value.trim(), family: family.value.trim(), lien: lien.value,
  })
  const r = await fetch(`${API}/api/signup?${q}`, { method: 'POST' })
  if (!r.ok) {
    const d = await r.json().catch(() => ({}))
    error.value = d.detail || 'Impossible de créer le compte.'; return
  }
  const data = await r.json()
  setToken(data.token); setMe(data)
  router.push('/famille')
}
</script>

<template>
  <div class="auth">
    <div class="hero">
      <div class="logo">
  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" width="34" height="34">
    <path d="M3 11L12 3L21 11" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M5 9.5V20C5 20.5523 5.44772 21 6 21H9C9.55228 21 10 20.5523 10 20V15C10 14.4477 10.4477 14 11 14H13C13.5523 14 14 14.4477 14 15V20C14 20.5523 14.4477 21 15 21H18C18.5523 21 19 20.5523 19 20V9.5"
          stroke="#7DD3FC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</div>
      <h1>Créer ma famille</h1>
      <p>Tu seras l'<strong>admin</strong> : tu créeras ensuite les comptes de tes proches.</p>
    </div>

    <div class="panel">
      <h2>Nouveau compte</h2>
      <label>Nom de la famille</label>
      <input v-model="family" placeholder="ex : Durand" />
      <label>Ton prénom</label>
      <input v-model="name" placeholder="ex : Maman" />
      <label>Ton lien de parenté</label>
      <select v-model="lien"><option v-for="l in LIENS" :key="l" :value="l">{{ l }}</option></select>
      <label>Email</label>
      <input v-model="email" type="email" autocomplete="email" placeholder="ex : maman@durand.fr" />
      <label>Mot de passe</label>
      <input v-model="password" type="password" autocomplete="new-password" placeholder="••••••" @keyup.enter="submit" />
      <button class="primary block" @click="submit">Créer ma famille</button>
      <p class="err" v-if="error">{{ error }}</p>
      <p class="switch">Déjà un compte ? <router-link to="/login">Se connecter</router-link></p>
    </div>
  </div>
</template>
