import { ref, type Ref, type UnwrapRef } from 'vue'

export default function useDataFetch<T>(
  url: string,
  params: string | string[][] | Record<string, string> | URLSearchParams | undefined
): {
  data: Ref<UnwrapRef<T> | null>
  fetchData: (
    params: string | Record<string, string> | URLSearchParams | string[][] | undefined
  ) => void
  isLoading: Ref<boolean>
  error: Ref<boolean>
} {
  const data = ref<T | null>(null)
  const isLoading = ref(true)
  const error = ref(false)

  const fetchData = (
    params: string | Record<string, string> | URLSearchParams | string[][] | undefined
  ) => {
    const qs = '?' + new URLSearchParams(params).toString()
    isLoading.value = true
    error.value = false

    fetch(url + qs)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Response not successful')
        }
        return response.json()
      })
      .then((result) => {
        data.value = result as UnwrapRef<T>
      })
      .catch(() => {
        error.value = true
      })
      .finally(() => {
        isLoading.value = false
      })
  }

  fetchData(params)

  return { data, fetchData, isLoading, error }
}
