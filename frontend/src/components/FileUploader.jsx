export function FileUploader({ onFileSelect, loading }) {
  function handleChange(e) {
    const file = e.target.files[0]
    if (file) onFileSelect(file)
  }

  return (
    <div className="flex flex-col items-center gap-4">
      <label className="cursor-pointer bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition">
        {loading ? "Analisando..." : "Selecionar arquivo .bin"}
        <input
          type="file"
          accept=".bin"
          onChange={handleChange}
          disabled={loading}
          className="hidden"
        />
      </label>
    </div>
  )
}