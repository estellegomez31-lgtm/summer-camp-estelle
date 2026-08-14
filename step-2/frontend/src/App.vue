<script setup>
import { ref } from 'vue'
import TaskList from './components/TaskList.vue'


/* Liste réactive de tâches */
const tasks = ref([
  { id: 1, title: 'Sortir les poubelles', done: false },
  { id: 2, title: 'Faire les courses', done: true }
])

/* Champ texte pour ajouter une nouvelle tâche */
const newTask = ref('')

/* Ajout d'une nouvelle tâche */
function addTask() {
  if (newTask.value.trim() === '') return

  tasks.value.push({
    id: Date.now(),
    title: newTask.value,
    done: false
  })

  newTask.value = ''
}

/* Suppression d'une tâche */
function deleteTask(id) {
  tasks.value = tasks.value.filter(t => t.id !== id)
}

function toggleTask(id) {
  const task = tasks.value.find(t => t.id === id)
  task.done = !task.done
}


</script>

<template>
  <header>
    <h1>🏠 FamilyTask</h1>
  </header>

  <main>
    <div class="card">
      <h2>Ma todo‑list 📝</h2>


      <!-- Champ + bouton -->
      <input v-model="newTask" type="text" placeholder="Nouvelle tâche..." />
      <button @click="addTask">Ajouter</button>

       <TaskList :tasks="tasks" @toggle="toggleTask" @remove="deleteTask" />

    </div>
  </main>
</template>
