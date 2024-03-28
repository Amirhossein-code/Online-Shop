# E-Commerce Website

## Description

An e-commerce website with all essential features.

## Authentication

- Email and password authentication with SimpleJwt.
- Users can log in, sign up, and update their credentials.
- Password reset: Users request a password reset by providing their email. An email containing a URL with a token is sent for password reset. The token in the URL is used for authentication during password reset.
- Welcome email feature implemented.

## Products

- Admins can create products, categorize them, set discounts, create discount codes for carts, feature products in hot list, and manage product status effectively.

## Client Side

- After registration, a user profile called Customer is created.
- Customers can submit reviews, which are displayed only after admin approval.
- Customers can create addresses and set one as their main address.
- Customers can purchase products via the purchase system.

## Purchase System

- Both anonymous and authenticated users can create carts and add products.
- When users want to complete a purchase, the cart ID is posted to the Orders endpoint.
- Anonymous users need to register at this point.
- An order is created with the cart and cart items, and the user is redirected to the payment gateway.
- Upon successful purchase, a ship object is created to notify the admin to ship the items, and the inventory is updated.
