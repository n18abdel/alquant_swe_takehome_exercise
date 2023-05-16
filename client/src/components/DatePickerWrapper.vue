<script setup lang="ts">
defineProps({
  modelValue: String
})
defineEmits(['update:modelValue'])

const yesterday = new Date(Date.now() - 86400000).toLocaleDateString('fr-ca')
</script>

<template>
  <div class="flex flex-col justify-center h-screen">
    <div class="flex justify-center mb-10">
      <label for="start" class="mr-2">Start date:</label>
      <input
        type="date"
        id="start"
        :value="modelValue"
        @input="$emit('update:modelValue', ($event.target as HTMLInputElement)?.value)"
        :max="yesterday"
      />
    </div>
    <slot></slot>
  </div>
</template>
