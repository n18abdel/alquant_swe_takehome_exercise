<script setup lang="ts">
import { ref, watch } from 'vue'
import Plotly from 'plotly.js-dist-min'
import LoadingSpinner from '@/components/LoadingSpinner.vue'
import ErrorBox from '@/components/ErrorBox.vue'
import FadeIn from '@/components/FadeIn.vue'

type StockData = {
  stocks: {
    [symbol: string]: number[]
  }
  timestamps: string[]
}

const container = ref<HTMLDivElement>()
const data = ref<StockData | null>(null)
const isLoading = ref(true)
const error = ref(false)
const errorMessage = 'Error! Could not retrieve performance data.'

fetch('/stocks/performance')
  .then((response) => response.json())
  .then((result) => {
    data.value = result as StockData
  })
  .catch(() => {
    error.value = true
  })
  .finally(() => {
    isLoading.value = false
  })

watch(data, (newValue) => {
  if (newValue) {
    const traces = Object.keys(newValue.stocks).map((symbol) => ({
      name: symbol,
      x: newValue.timestamps,
      y: newValue.stocks[symbol]
    }))
    Plotly.newPlot(container.value as Plotly.Root, traces)
  }
})
</script>

<template>
  <div class="flex justify-center items-center h-screen">
    <FadeIn v-show="!isLoading && !error"><div ref="container"></div></FadeIn>
    <FadeIn v-show="!isLoading && error"
      ><ErrorBox class="h-1/4 w-1/3 justify-center" :message="errorMessage"
    /></FadeIn>
    <LoadingSpinner v-if="isLoading" />
  </div>
</template>
