const express = require('express');
const express = require('express');
const router = express.Router();
const Product = require('../models/Product');

router.get('/products', async (req, res) => {
  const products = await Product.find();
  res.json(products);
});

router.get('/products/:id', async (req, res) => {
  const product = await Product.findById(req.params.id);
  res.json(product);
});

router.post('/products', async (req, res) => {
  const product = new Product(req.body);
  await product.save();
  res.json(product);
});

router.put('/products/:id', async (req, res) => {
  const product = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(product);
});

router.delete('/products/:id', async (req, res) => {
  await Product.findByIdAndRemove(req.params.id);
  res.json({ message: 'Product deleted successfully' });
});

module.exports = router;