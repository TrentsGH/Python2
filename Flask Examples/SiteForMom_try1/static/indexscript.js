let slideIndex = 1;
showSlides();

function showSlides() {
            let i;
            var slides = document.getElementsByClassName("mySlides");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
                if (i== slideIndex){
                    slides[i].style.display = "block";
                }
                
            }
            slideIndex++;
            if (slideIndex > slides.length-1) {
                slideIndex = 0;
            }
            
            //slides[1].style.display = "block";
            setTimeout(showSlides, 2000); // Change slide every 2 seconds
        }

