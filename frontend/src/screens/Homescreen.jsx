import React, {useState, useEffect} from 'react'
import { Row, Col } from 'react-bootstrap'
// import products from '../products'
import Product from '../components/Product'
import axios from 'axios'
import { useDispatch, useSelector } from 'react-redux'
import { listProducts } from '../actions/productActions';

function HomeScreen() {
  const dispatch = useDispatch()
  const productList = useSelector(state => state.productList)
  const { error, loading, } = productList
  useEffect(() => {
    dispatch(listProducts())
  }, [])

  const [products, setProducts] = useState([])
  useEffect(() => {
    async function fetchProducts()  {
      const { data } = await axios.get('http://127.0.0.1:8000/api/products/');
      setProducts(data);
    };

    fetchProducts();
  }, []);

  return (
    <div>
        <h1>Latest Gabby Products</h1>
        <Row>
            {products.map(product =>(
                <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
                    <Product product = {product} />
                </Col>
                ))}
        </Row>
    </div>
  )
}

export default HomeScreen


