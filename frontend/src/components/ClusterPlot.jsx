export function ClusterPlot({ plot }) {
  return (
    <div className="flex flex-col items-center gap-2">
      <h2 className="text-gray-400 text-sm font-semibold uppercase tracking-wide">
        Clusterização
      </h2>
      <img
        src={plot}
        alt="Cluster plot"
        className="rounded-lg max-w-full border border-gray-700"
      />
    </div>
  )
}