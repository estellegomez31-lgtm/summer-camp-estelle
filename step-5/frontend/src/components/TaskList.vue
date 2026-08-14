<script setup>
const props = defineProps({
  tasks: Array,
  members: { type: Array, default: () => [] }
})
const emit = defineEmits(['toggle', 'remove'])

function memberName(id) {
  const m = props.members.find(m => m.id === id)
  return m ? m.name : ''
}
</script>

<template>
  <ul class="tasklist">
    <li v-for="t in props.tasks" :key="t.id">
      <span :class="{ done: t.done }">{{ t.title }}</span>
      <small> → {{ memberName(t.member_id) }}</small>

      <button @click="emit('toggle', t.id)">✔</button>
      <button @click="emit('remove', t.id)">🗑</button>
    </li>
  </ul>
</template>

<style scoped>
.tasklist {
  list-style: none;
  padding: 0;
}
.done {
  text-decoration: line-through;
}
</style>
