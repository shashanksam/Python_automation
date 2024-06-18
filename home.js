// import React from "react";


/* WORKING
*/
let currentSlide = 0;
const images = ['/assets/assets/home.jpg', '/assets/assets/home1.jpg', '/assets/assets/home2.jpg'];

function showSlide(index) {
    document.body.style.backgroundImage = `url(${images[index]})`;
    document.body.style.backgroundSize = 'cover';
    document.body.style.backgroundPosition = 'center 50%';
    document.body.style.backgroundRepeat = 'no-repeat'; // Prevent the background image from tiling

}

function nextSlide() {
    currentSlide = (currentSlide + 1) % images.length;
    showSlide(currentSlide);
}

setInterval(nextSlide, 1000);


