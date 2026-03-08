import React from "react";
import { Line } from "react-chartjs-2";

const PriceChart = ({ products }) => {
  const prices = products.map((p) => p.price || 0);
  const ids = products.map((p) => p.id);

  const data = {
    labels: ids,
    datasets: [
      {
        label: "Price of Products",
        data: prices,
        borderColor: "rgba(255, 99, 132, 0.8)",
        fill: false,
      },
    ],
  };

  return <Line data={data} />;
};

export default PriceChart;