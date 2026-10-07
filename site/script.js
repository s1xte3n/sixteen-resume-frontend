(() => {
  "use strict";

  const countElement = document.getElementById("visitor-count");
  const statusElement = document.getElementById("visitor-status");
  const endpoint = new URL("/api/visitors", window.location.origin).toString();

  if (!countElement || !statusElement) return;

  const requestId = crypto.randomUUID ? crypto.randomUUID() : null;

  fetch(endpoint, {
    method: "GET",
    headers: requestId ? { "X-Request-ID": requestId } : {}
  })
    .then(async (response) => {
      const body = await response.json().catch(() => null);

      if (!response.ok || !body || !Number.isInteger(body.count) || body.count < 0) {
        throw new Error("Visitor counter request failed.");
      }

      return body;
    })
    .then((body) => {
      countElement.textContent = body.count.toLocaleString();
      statusElement.textContent = "Live";
    })
    .catch(() => {
      countElement.textContent = "—";
      statusElement.textContent = "Unavailable";
    });
})();
