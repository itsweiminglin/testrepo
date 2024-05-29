<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wei Ming Lin Portfolio Website</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css">
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.css" integrity= "sha256-46qynGAkLSFpVbEBog43gvNhfrOj+BmwXdxFgVK/Kvc=" crossorigin="anonymous" />


    </head>
    <body>
        <header>
            <div class="logo">
                <img src="img/weiming.png" alt="">
            </div>
            <button class="nav-toggle" aria-label="toggle navigation">
                <span class="hamburger"></span>
            </button>
            <nav class="nav">
                <ul class="nav__list">
                    <li class="nav__item"><a href="#home" class="nav__link">Home</a></li>
                    <li class="nav__item"><a href="#services" class="nav__link">My Services</a></li>
                    <li class="nav__item"><a href="#me" class="nav__link">About Me</a></li>
                    <li class="nav__item"><a href="#work" class="nav__link">My Work</a></li>
                </ul>
            </nav>
        </header>

        <!--Introduction--> 
        <section class="intro" id="home">
            <h1 class="section__title section__title--intro">
                Hello, I am <strong>Wei Ming Lin</strong>
            </h1>
            <p class="section__subtitle section__subtitle--intro">Full Stack Dev</p>
            <img src="img/weiming-01.jpg" alt="a picture of Wei Ming smiling">
        </section>


        <!-- My Services -->
        <section class="my-services" id="services">
            <h2 class="section__title section__title--services">What I Do</h2>
            <div class="services">
                <div class="services">
                    <h3>Design + Development</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt</p>
                </div> <!--/ service-->

                <div class="services">
                    <h3>E-Commerce</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt</p>
                </div> <!--/ service-->

                <div class="services">
                    <h3></h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt</p>
                </div> <!--/ service-->
            </div> <!--/ services-->

            <a href="#work" class="btn">My Work</a>
        </section>


        <!-- About Me -->
        <section class="about-me" id="me">
            <h2 class="section__title section__title--me">Who I Am</h2>
            <p class="section__subtitle section__subtitle--me"></p>

            <div class="about-me__body">
                <p>As an aspiring software developer, I am driven by a deep curiosity and passion for technology. 
                    I am committed to acquiring a diverse skill set encompassing programming languages, frameworks, and best practices. 
                    With a foundation built on enthusiasm and determination, I approach each new concept as an exciting challenge to conquer. 
                    My goal is not just to write code, but to understand the principles behind it, enabling me to build innovative solutions that solve real-world problems.</p>
            </div>
            <img src="img/weiming-02.jpg" alt="Weiming leaning against car">
        </section>
    </body>
</html>
