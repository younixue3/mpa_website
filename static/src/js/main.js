// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    let video = document.querySelector("#scrollVideo");
    let videoSection = document.querySelector("section");
    const batu1 = document.getElementById('batu1');
    const batu2 = document.getElementById('batu2');
    const batu3 = document.getElementById('batu3');
    const batu4 = document.getElementById('batu4');
    const batu5 = document.getElementById('batu5');
    const batu6 = document.getElementById('batu6');
    const batu7 = document.getElementById('batu7');
    let maxVideoTime = 9; // Maximum video duration in seconds
    let exactTime = 0.0; // Time in seconds with millisecond precision
    let lastScrollPosition = window.scrollY;
    let animationFrameId;
    let lastTimestamp = 0;

    // Only add scroll listener if required elements exist
    if (video && videoSection && wrapwrap) {
        // Throttle scroll events using timestamp
        wrapwrap.addEventListener('scroll', function() {
            // Cancel any pending animation frame
            if (animationFrameId) {
                cancelAnimationFrame(animationFrameId);
            }

            const now = performance.now();
            if (now - lastTimestamp < 16) { // Skip if less than 16ms (60fps)
                return;
            }
            lastTimestamp = now;

            // Use requestAnimationFrame for smooth 60fps updates
            animationFrameId = requestAnimationFrame(() => {
                // Get the section's position relative to viewport
                const sectionRect = videoSection.getBoundingClientRect();
                const currentScrollPosition = window.scrollY;
                
                if (sectionRect.top >= 0) {
                    // Increase time increment for faster playback
                    const timeIncrement = 0.01; // Quadruple the speed (1/15th of a second)
                    exactTime = Math.min((exactTime + timeIncrement), maxVideoTime);
                    
                    // Use RAF to batch video time updates
                    if (video.readyState >= 2) { // Check if video is loaded
                        video.currentTime = exactTime;
                    }
                    // Handle batu elements visibility based on video time

                    console.log(exactTime)
                    // Show/hide elements based on video time
                    if (exactTime > 3 && exactTime < 3.8) {
                        batu1.classList.remove('hidden');
                    } else if (exactTime > 3.8 && exactTime < 4.6) {
                        batu1.classList.add('hidden');
                        batu2.classList.remove('hidden');
                    } else if (exactTime > 4.6 && exactTime < 5.4) {
                        batu2.classList.add('hidden');
                        batu3.classList.remove('hidden');
                    } else if (exactTime > 5.5 && exactTime < 6) {
                        batu3.classList.add('hidden');
                        batu4.classList.remove('hidden');
                    } else if (exactTime > 6.35 && exactTime < 7) {
                        batu4.classList.add('hidden');
                        batu5.classList.remove('hidden');
                    } else if (exactTime > 7.4 && exactTime < 8) {
                        batu5.classList.add('hidden');
                        batu6.classList.remove('hidden');
                    } else if (exactTime > 8 && exactTime <= 9) {
                        batu6.classList.add('hidden');
                        batu7.classList.remove('hidden');
                    }
                }

                // Determine scroll direction
                if (currentScrollPosition > lastScrollPosition) {
                    // Scrolling down
                } else {
                    // Scrolling up
                }
                
                lastScrollPosition = currentScrollPosition;
            });
        }, { passive: true }); // Add passive flag for better scroll performance

        // Cleanup animation frame on page unload
        window.addEventListener('unload', () => {
            if (animationFrameId) {
                cancelAnimationFrame(animationFrameId);
            }
        });
    }
});