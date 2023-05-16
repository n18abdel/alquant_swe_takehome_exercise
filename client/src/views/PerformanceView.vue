<script setup lang="ts">
import { ref, watch } from 'vue'
import Plotly from 'plotly.js-dist-min'
import useDataFetch from '@/composables/useDataFetch'
import useStartDate from '@/composables/useStartDate'
import DatePickerWrapper from '@/components/DatePickerWrapper.vue'
import DataLoader from '@/components/DataLoader.vue'

type StockData = {
  stocks: {
    [symbol: string]: number[]
  }
  timestamps: string[]
}

const container = ref<HTMLDivElement>()
const initialDate = new Date(new Date().getFullYear() - 1, 0, 1).toLocaleDateString('fr-ca')
const { data, fetchData, isLoading, error } = useDataFetch<StockData>('/stocks/performance', {
  start: initialDate
})
const errorMessage = 'Error! Could not retrieve performance data.'
const startDate = useStartDate(initialDate, fetchData)

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
  <DatePickerWrapper v-model="startDate">
    <DataLoader v-bind="{ isLoading, error, errorMessage }">
      <div ref="container"></div>
    </DataLoader>
  </DatePickerWrapper>
</template>
