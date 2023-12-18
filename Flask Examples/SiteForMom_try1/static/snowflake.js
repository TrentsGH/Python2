document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('snowflakes-container');
            
    function createSnowflake() {
                    const snowflake = document.createElement('div');
                    snowflake.className = 'snowflake';
                    snowflake.style.left = `${Math.random() * 100}vw`;
                    container.appendChild(snowflake);
                    setTimeout(() => {
                        container.removeChild(snowflake);
                    }, 5000); // Adjust the duration the snowflake is visible
                }
            
                function createSnowfall() {
                    setInterval(createSnowflake, 2000); // Adjust the interval to control the frequency of snowflakes
                }
                
                createSnowfall();
            });