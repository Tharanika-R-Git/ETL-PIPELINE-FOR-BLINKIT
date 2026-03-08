import './chartSetup.js';
import React, { useEffect, useState } from "react";
import { fetchProducts } from "./api";
import ProductsTable from "./components/ProductsTable";
import CategoryChart from "./components/CategoryChart";
import PriceChart from "./components/PriceChart";

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const loadData = async () => {
      const data = await fetchProducts();
      setProducts(data);
    };
    loadData();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Blinkit Products Dashboard</h1>
      <h2>Products Table</h2>
      <ProductsTable products={products} />
      <h2>Products by Category</h2>
      <CategoryChart products={products} />
      <h2>Products Price Chart</h2>
      <PriceChart products={products} />
    </div>
  );
}

export default App;