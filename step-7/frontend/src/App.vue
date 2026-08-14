<script setup>
import { useRoute, useRouter } from 'vue-router'
import { isLogged, getMe, logout as apiLogout } from './api.js'

const route = useRoute()
const router = useRouter()

function logout() {
  apiLogout()
  router.push('/login')
}
</script>

<template>
  <div class="phone">

    <!-- HEADER -->
    <header class="appbar" v-if="isLogged() && route.meta.nav">
      <div class="brand">
        <svg class="brand-icon" viewBox="0 0 24 24" fill="none">
          <path d="M3 11L12 3L21 11"
                stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          <path d="M5 9.5V20C5 20.5523 5.44772 21 6 21H9C9.55228 21 10 20.5523 10 20V15C10 14.4477 10.4477 14 11 14H13C13.5523 14 14 14.4477 14 15V20C14 20.5523 14.4477 21 15 21H18C18.5523 21 19 20.5523 19 20V9.5"
                stroke="#7DD3FC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        FamilyTask
      </div>

      <button class="link" @click="logout">Quitter</button>
    </header>

    <!-- CONTENU -->
    <main class="screen">
      <router-view />
    </main>

    <!-- TABBAR -->
    <nav class="tabbar" v-if="isLogged() && route.meta.nav">

      <!-- TÂCHES -->
      <router-link to="/taches" class="tab">
        <span class="ico">
          <svg width="22" height="22" fill="none" stroke="#1E3A8A" stroke-width="2" stroke-linecap="round">
            <path d="M4 6h14M4 12h14M4 18h10"></path>
          </svg>
        </span>
        Tâches
      </router-link>

      <!-- ASSISTANT -->
      <router-link to="/assistant" class="tab">
        <span class="ico">
          <svg width="22" height="22" fill="none" stroke="#F97316" stroke-width="2" stroke-linecap="round">
            <path d="M4 4h16v10H10l-6 6V4z"></path>
          </svg>
        </span>
        Assistant
      </router-link>

      <!-- FAMILLE (admin seulement) -->
      <router-link v-if="getMe() && getMe().is_admin" to="/famille" class="tab">
        <span class="ico">
          <svg width="22" height="22" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round">
            <circle cx="11" cy="6" r="3"></circle>
            <path d="M3 20c0-4 3-6 8-6s8 2 8 6"></path>
          </svg>
        </span>
        Famille
      </router-link>

    </nav>

  </div>
</template>

<style>
/* --- TABBAR ANIMÉE --- */

.tabbar {
  display: flex;
  justify-content: space-around;
  background: #0f172a;
  padding: 8px 0;
}

.tab {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #94a3b8;
  font-size: 12px;
  transition: all 0.25s ease;
}

.tab .ico svg {
  transition: transform 0.25s ease, opacity 0.25s ease;
}

.tab.router-link-active {
  color: #fff;
  transform: translateY(-3px);
}

.tab.router-link-active .ico svg {
  transform: scale(1.25);
  opacity: 1;
}

/* --- GLOW ANIMATION --- */

.tab.router-link-active {
  position: relative;
}

.tab.router-link-active::before {
  content: "";
  position: absolute;
  bottom: -2px;
  width: 30px;
  height: 3px;
  border-radius: 3px;
  background: currentColor;
  animation: glow 0.3s ease-out;
}

@keyframes glow {
  from { opacity: 0; transform: scaleX(0.2); }
  to { opacity: 1; transform: scaleX(1); }
}
</style>
