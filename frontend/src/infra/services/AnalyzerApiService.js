const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1"

export async function analyzeBinary(file) {
  const formData = new FormData()
  formData.append("file", file)

  const response = await fetch(`${API_URL}/analyze`, {
    method: "POST",
    body: formData,
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.detail || "Erro ao analisar arquivo")
  }

  return response.json()
}