// JavaScript para abrir e fechar o menu mobile
const menuBtn = document.getElementById('menu-btn');
const navbar = document.querySelector('.navbar');

menuBtn.addEventListener
('click', () => { navbar.classList.toggle('show')});

// JavaScript para abrir e fechar a barra de pesquisa
const searchBtn = document.getElementById('search-btn');
const searchForm = document.querySelector('.search-form');

searchBtn.addEventListener
('click', () => {searchForm.classList.toggle('show')});
