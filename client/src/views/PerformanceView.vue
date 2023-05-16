<script setup lang="ts">
import { ref, watch } from 'vue'
import Plotly from 'plotly.js-dist-min'
import useDataFetch from '@/composables/useDataFetch'
import DataLoader from '@/components/DataLoader.vue'

type StockData = {
  stocks: {
    [symbol: string]: number[]
  }
  timestamps: string[]
}

const container = ref<HTMLDivElement>()
const { data, isLoading, error } = useDataFetch<StockData>('/stocks/performance')
const errorMessage = 'Error! Could not retrieve performance data.'

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
  <DataLoader v-bind="{ isLoading, error, errorMessage }"><div ref="container"></div></DataLoader>
</template>
