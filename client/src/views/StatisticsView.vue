<script setup lang="ts">
import { ref } from 'vue'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import ErrorBox from '@/components/ErrorBox.vue'
import FadeIn from '@/components/FadeIn.vue'
import DataTable from '@/components/DataTable.vue'
import { type TableData } from '@/components/DataTable.vue'

type StatsData = {
  [symbol: string]: {
    [stat: string]: number
  }
}

const data = ref<StatsData | null>(null)
const isLoading = ref(true)
const error = ref(false)
const errorMessage = 'Error! Could not retrieve statistics data.'

fetch('/stocks/statistics')
  .then((response) => response.json())
  .then((result) => {
    data.value = result as StatsData
  })
  .catch(() => {
    error.value = true
  })
  .finally(() => {
    isLoading.value = false
  })
</script>

<template>
  <div class="h-screen flex items-center justify-center">
    <FadeIn v-show="!isLoading && !error"
      ><DataTable v-if="data" :data="(data as TableData)"
    /></FadeIn>
    <FadeIn v-show="!isLoading && error"
      ><ErrorBox class="h-1/4 w-1/3 justify-center" :message="errorMessage"
    /></FadeIn>
    <LoadingSpinner v-if="isLoading" />
  </div>
</template>
