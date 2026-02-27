import { useAnalyzer } from "../hooks/useAnalyzer"
import { FileUploader } from "../components/FileUploader"
import { ResultFolder } from "../components/ResultFolder"

export function HomePage() {
  const { result, loading, error, analyze } = useAnalyzer()

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center py-16 px-4 gap-8">
      <div className="flex flex-col items-center gap-2">
        <h1 className="text-3xl font-bold">Binary Analyzer</h1>
        <p className="text-gray-400">Faça upload de um arquivo .bin para analisar</p>
      </div>

      <FileUploader onFileSelect={analyze} loading={loading} />

      {error && (
        <div className="bg-red-900 border border-red-700 text-red-300 px-4 py-3 rounded-lg">
          {error}
        </div>
      )}

      {result && <ResultFolder result={result} />}
    </div>
  )
}