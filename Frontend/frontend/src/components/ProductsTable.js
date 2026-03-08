import React from "react";

const ProductsTable = ({ products }) => {
  return (
    <div style={{ maxHeight: "400px", overflowY: "scroll" }}>
      <table border="1" width="100%" cellPadding="5">
        <thead>
          <tr>
            <th>ID</th>
            <th>Collection</th>
            <th>Name</th>
            <th>Category</th>
            <th>Price</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p) => (
            <tr key={p.id}>
              <td>{p.id}</td>
              <td>{p.collection}</td>
              <td>{p.product_name}</td>
              <td>{p.category}</td>
              <td>{p.price}</td>
              <td>{p.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductsTable;