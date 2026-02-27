const LABELS = {
  header: { label: "Header", color: "bg-blue-500" },
  raw_data: { label: "Raw Data", color: "bg-green-500" },
  offset: { label: "Offset", color: "bg-yellow-500" },
}

export function SummaryCards({ summary }) {
  return (
    <div className="grid grid-cols-3 gap-4">
      {Object.entries(summary).map(([key, value]) => (
        <div key={key} className="bg-gray-800 rounded-lg p-4 flex flex-col items-center gap-2">
          <div className={`w-3 h-3 rounded-full ${LABELS[key].color}`} />
          <span className="text-gray-400 text-sm">{LABELS[key].label}</span>
          <span className="text-white text-2xl font-bold">{value}</span>
          <span className="text-gray-500 text-xs">blocos</span>
        </div>
      ))}
    </div>
  )
}