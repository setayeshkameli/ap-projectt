function openSlideMenu() {
    document.getElementById('side-menu').style.width = '250px';
}

function closeSlideMenu() {
    document.getElementById('side-menu').style.width = '0';
}
var slideIndex = 1;

showSlides(slideIndex);

function plusSlide(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("slide-img");
    if (n > slides.length) {slideIndex = 1}    
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slides[slideIndex-1].style.display = "block";  
}