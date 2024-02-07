import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom'; // Import useNavigate hook
import { useDispatch, useSelector } from 'react-redux';
import { addToCart } from '../actions/cartActions';

const ProductScreen = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate(); // Initialize useNavigate hook
  const [product, setProduct] = useState(null);
  const [qty, setQty] = useState(1);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/products/${id}`);
        if (!response.ok) {
          throw new Error(`Failed to fetch product. Status: ${response.status}`);
        }
        const data = await response.json();
        setProduct(data);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  const handleAddToCart = () => {
    dispatch(addToCart(id, qty));
    navigate('/cart'); // Use navigate to navigate to '/cart' route
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!product) {
    return <div>No product found</div>;
  }


  return (
    <div>
      <h1>{product.name}</h1>
      <img src={product.image} alt={product.name} />
      <p>{product.description}</p>
      <p>{product.price}</p>

      <div>
        <label>Quantity:</label>
        <select value={qty} onChange={(e) => setQty(Number(e.target.value))}>
          {[...Array(product.countInStock).keys()].map((x) => (
            <option key={x + 1} value={x + 1}>
              {x + 1}
            </option>
          ))}
        </select>
      </div>

      <button onClick={handleAddToCart}>Add to Cart</button>
    </div>
  );
};

export default ProductScreen;
