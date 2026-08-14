<script setup>
import { useRouter } from 'vue-router'
import { isLogged, getMe, logout as apiLogout } from './api.js'

const router = useRouter()
const me = getMe()

function logout() {
  apiLogout()
  router.push('/login')
}
</script>

<template>
  <div class="phone">
    <!-- Barre du haut -->
    <div class="appbar">
      <div class="brand">FamilyTask</div>
      <button class="link" @click="logout">Quitter</button>
    </div>

    <!-- Contenu de l'écran -->
    <div class="screen">
      <router-view />
    </div>

    <!-- Barre d'onglets -->
    <div class="tabbar" v-if="isLogged">
      <router-link class="tab" to="/taches">
        <div class="ico">📋</div>
        Tâches
      </router-link>

      <router-link class="tab" to="/famille" v-if="me && me.is_admin">
        <div class="ico">👨‍👩‍👧</div>
        Famille
      </router-link>
    </div>
  </div>
</template>
