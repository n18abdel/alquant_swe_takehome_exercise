import { ref, type Ref, type UnwrapRef } from 'vue'

export default function useDataFetch<T>(url: string): {
  data: Ref<UnwrapRef<T> | null>
  isLoading: Ref<boolean>
  error: Ref<boolean>
} {
  const data = ref<T | null>(null)
  const isLoading = ref(true)
  const error = ref(false)

  fetch(url)
    .then((response) => response.json())
    .then((result) => {
      data.value = result as UnwrapRef<T>
    })
    .catch(() => {
      error.value = true
    })
    .finally(() => {
      isLoading.value = false
    })

  return { data, isLoading, error }
}
