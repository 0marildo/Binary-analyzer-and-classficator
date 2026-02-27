import { useState } from "react"
import { analyzeBinary } from "../infra/services/AnalyzerApiService"

export function useAnalyzer() {
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  async function analyze(file) {
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const data = await analyzeBinary(file)
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return { result, loading, error, analyze }
}