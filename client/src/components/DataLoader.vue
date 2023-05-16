<script setup lang="ts">
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import ErrorBox from '@/components/ErrorBox.vue'
import FadeIn from '@/components/FadeIn.vue'

defineProps({
  isLoading: Boolean,
  error: Boolean,
  errorMessage: String
})
</script>

<template>
  <div class="flex justify-center items-center w-full">
    <FadeIn v-show="!isLoading && !error"><slot></slot></FadeIn>
    <FadeIn v-show="!isLoading && error"
      ><ErrorBox class="h-full w-1/3 justify-center" :message="errorMessage"
    /></FadeIn>
    <LoadingSpinner v-if="isLoading" />
  </div>
</template>
