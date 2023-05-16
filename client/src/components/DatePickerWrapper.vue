<script setup lang="ts">
import { ref } from 'vue'

defineProps({
  modelValue: String
})
defineEmits(['update:modelValue'])

const yesterday = new Date(Date.now() - 86400000).toLocaleDateString('fr-ca')
const debounceTimeout = ref<number | null>(null)

function debounce(func: Function, delay: number) {
  if (debounceTimeout.value) {
    clearTimeout(debounceTimeout.value)
  }
  debounceTimeout.value = setTimeout(func, delay)
}
</script>

<template>
  <div class="flex flex-col justify-center h-screen">
    <div class="flex justify-center mb-10">
      <label for="start" class="mr-2">Start date:</label>
      <input
        type="date"
        id="start"
        :value="modelValue"
        @input="
          debounce(() => {
            $emit('update:modelValue', ($event.target as HTMLInputElement)?.value)
          }, 1000)
        "
        :max="yesterday"
      />
    </div>
    <slot></slot>
  </div>
</template>
