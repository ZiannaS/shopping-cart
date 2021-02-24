# SHOPPING CART APPLICATION

OVERVIEW: 
This simple shopping cart application automates the cumbersome process of checking out at a local grocery store. It employs real life features of self checkout making the user experience seamless and easy. Users can simply input the the unique identifier of the product they have purchased. The application will then acquire all the details of the product and add it to the user's cart for checkout. Once the user has inputed the unique id for each of their items, the user can type "DONE" to finish the checkout process. One can even choose to have their receipt emailed to them by answering "yes" to the prompt asking for the same. The user's receipt is also stored into a folder on the grocery store computer for store owners to go over the receipts later on. Lastly, I wanted the product to be applicable nationwide and thus allow for store owners to set the sales tax for their required states. 

FEATURES
- Identify products simply through the numeric unique identifier.
- Create a human friendly recript.
- Email the receipt to the buyers.
- Keep the receipt stored for a later date on the local computer.

ENVIRONMENT VARIABLE SET UP 
- Create a .env file in the root directory of the project. 
- Ensure that this file is named “.env” 
- Within the env file add the following fields: 
    - SENDGRID_API_KEY=*The API KEY OF YOUR SENDGRID ACCOUNT* 
    - SENDER_ADDRESS=*THE EMAIL THROUGH WHICH YOU WANT TO SEND ALL RECEIPTS*
    - TAX_RATE=*THE TAX RATE FOR WHICHEVER STATE YOU ARE A PART OF*
- Save this in the same directory as the python script and your checkout service is ready!