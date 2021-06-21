console.log("Sanity check!");

// new
// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  // new
  // Event handler
  document.querySelector("#purchaseBasic").addEventListener("click", () => {
    // Get Checkout Session ID
    
    fetch("/create-checkout-session/?price=50000&plan=Basic Storage - 5 tb plan")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
  document.querySelector("#purchaseAdv").addEventListener("click", () => {
    // Get Checkout Session ID
    
    fetch("/create-checkout-session/?price=100000&plan=Advanced Storage - 10 tb plan")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
  document.querySelector("#purchasePrm").addEventListener("click", () => {
    // Get Checkout Session ID
    
    fetch("/create-checkout-session/?price=200000&plan=Premium Storage - 20 tb plan")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});