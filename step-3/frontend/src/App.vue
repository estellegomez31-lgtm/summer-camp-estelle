<script setup>
import TaskList from './components/TaskList.vue'
import { ref, onMounted } from 'vue'

// Données locales (pas encore de base de données) — juste pour construire l'interface.
const tasks = ref([])
const newTitle = ref('')
let nextId = 3

// Charger les tâches depuis l'API
async function loadTasks() {
  const res = await fetch('/api/tasks')
  tasks.value = await res.json()
}

// Ajouter une tâche
async function addTask() {
  if (!newTitle.value.trim()) return

  await fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      title: newTitle.value,
      done: false
    })
  })

  newTitle.value = ''
  loadTasks()  // ⭐ recharge la liste
}

// Cocher une tâche (PATCH)
async function toggleTask(id) {
  await fetch(`/api/tasks/${id}`, {
    method: 'PATCH'
  })

  loadTasks()  // ⭐ recharge la liste
}

// Supprimer une tâche (DELETE)
async function removeTask(id) {
  await fetch(`/api/tasks/${id}`, {
    method: 'DELETE'
  })

  loadTasks()  // ⭐ recharge la liste
}


onMounted(loadTasks)


</script>

<template>
  <header><h1>🏠 FamilyTask</h1></header>
  <main>
    <div class="card">
      <h2>Nouvelle tâche</h2>
      <div class="row">
        <input v-model="newTitle" placeholder="Ex: Sortir les poubelles" @keyup.enter="addTask" />
        <button @click="addTask">Ajouter</button>
      </div>
    </div>
    <div class="card">
      <h2>Les tâches</h2>
      <TaskList :tasks="tasks" @toggle="toggleTask" @remove="removeTask" />
    </div>
  </main>
</template>
