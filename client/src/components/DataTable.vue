<script setup lang="ts">
import { computed } from 'vue'

export type TableData = { [name: string]: { [column: string]: number } }

const props = defineProps({
  data: {
    type: Object as () => TableData,
    required: true
  }
})
const columns = computed(() =>
  Object.keys(Object.values(props.data)[0]).map((name) => name.replace('_', ' '))
)
const rows = computed(() => {
  return Object.entries(props.data).map(([name, values]) => ({
    name,
    values: Object.values(values)
  }))
})
</script>

<template>
  <div class="overflow-x-auto shadow-lg rounded-b-lg">
    <table class="table table-zebra table-normal">
      <thead>
        <tr>
          <th></th>
          <th v-for="column in columns" :key="column">{{ column }}</th>
        </tr>
      </thead>
      <tbody>
        <tr class="hover" v-for="row in rows" :key="row.name">
          <td>{{ row.name }}</td>
          <td v-for="value in row.values" :key="value">{{ value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
