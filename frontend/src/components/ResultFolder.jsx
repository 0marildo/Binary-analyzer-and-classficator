import { SummaryCards } from "./SummaryCards"
import { ClusterPlot } from "./ClusterPlot"

export function ResultFolder({ result }) {
  return (
    <div className="flex flex-col gap-6 w-full">
      <p className="text-gray-400 text-sm text-center">
        Total de blocos analisados:{" "}
        <span className="text-white font-semibold">{result.num_blocks}</span>
      </p>
      <SummaryCards summary={result.summary} />
      <ClusterPlot plot={result.plot} />
    </div>
  )
}