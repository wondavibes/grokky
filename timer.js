// Set the event date (from backend or hardcoded)
const eventDate = new Date("2025-12-31T00:00:00");

function updateCountdown() {
  const now = new Date();
  const diff = eventDate - now;

  if (diff <= 0) {
    document.getElementById("countdown").innerHTML = "Event has started!";
    return;
  }

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const mins = Math.floor((diff / (1000 * 60)) % 60);
  const secs = Math.floor((diff / 1000) % 60);

  document.getElementById("countdown").innerHTML =
    days + "d " + hours + "h " + mins + "m " + secs + "s left";
}

setInterval(updateCountdown, 1000);
updateCountdown();
