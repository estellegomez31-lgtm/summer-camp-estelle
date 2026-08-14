<template>
  <ul class="task-list">
    <template v-if="tasks?.length === 0">
      <li class="empty-state">✨ Votre liste est vide. Ajoutez une nouvelle tâche pour commencer !</li>
    </template>

    <template v-else>
      <li v-for="t in tasks" :key="t.id" class="task-item" :class="{ completed: t.done }">
        <label class="task-check">
          <input
            type="checkbox"
            :checked="t.done"
            @change="$emit('toggle', t.id)"
          />
          <span class="checkmark"></span>
        </label>

        <span :class="{ done: t.done }" class="task-title">
          {{ t.title }}
        </span>

        <button class="trash" @click="$emit('remove', t.id)" aria-label="Supprimer la tâche">🗑️</button>
      </li>
    </template>
  </ul>
</template>

<script setup>
defineProps({
  tasks: Array
})
</script>

<style>
.task-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.task-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  border-radius: 14px;
  background: var(--card);
  border: 1px solid var(--border);
  box-shadow: 0 4px 12px rgba(76, 55, 124, 0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.task-item:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(76, 55, 124, 0.12);
}

.task-item.completed {
  background: #f3f4f6;
  border-color: #e5e7eb;
}

.task-item.completed .task-title {
  color: #9ca3af;
}

.task-check {
  position: relative;
  display: inline-flex;
  align-items: center;
}

.task-check input {
  appearance: none;
  width: 18px;
  height: 18px;
  border: 2px solid #a78bfa;
  border-radius: 5px;
  cursor: pointer;
  margin: 0;
  transition: all 0.2s ease;
}

.task-check input:checked {
  background: linear-gradient(135deg, #8b5cf6, #ec4899);
  border-color: #8b5cf6;
}

.task-check input:checked + .checkmark::after {
  content: "✓";
  color: white;
  font-size: 12px;
  position: absolute;
  left: 3px;
  top: -1px;
}

.task-title {
  flex: 1;
  color: var(--text);
}

.empty-state {
  padding: 16px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px dashed var(--border);
  color: var(--muted);
  text-align: center;
  font-style: italic;
}

.done {
  text-decoration: line-through;
  opacity: 0.6;
}

.trash {
  margin-left: auto;
  background: linear-gradient(135deg, #ffb347, #ff6b6b);
  border: none;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  padding: 6px 8px;
  border-radius: 10px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.trash:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 10px rgba(255, 107, 107, 0.25);
}
</style>
