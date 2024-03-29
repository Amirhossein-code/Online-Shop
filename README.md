# E-Commerce Website

## Description

An e-commerce website with all essential features for a seamless shopping experience.

## Authentication

- Email and password authentication using SimpleJwt for secure user login, signup, and profile management.
- Password reset functionality allows users to request a password reset via email. An email containing a URL with a token is sent for password reset, ensuring secure authentication.
- Welcome email feature enhances user onboarding experience.

## Products

- Admins have the ability to create, categorize, set discounts, and feature products in hot lists. Advanced filtering options are available for effective product search and browsing.

## Client Side

- User profiles called Customers are automatically created upon registration.
- Customers can submit reviews for products, which are displayed only after admin approval.
- Address management feature allows customers to create addresses and set one as their main address for shipping convenience.
- Seamless purchase process enables customers to browse and purchase products efficiently.

## Purchase System

- Both anonymous and authenticated users can create carts, add products, and proceed to checkout.
- When users want to complete a purchase, the cart ID is posted to the Orders endpoint.
- Anonymous users are prompted to register before finalizing the purchase.
- Orders are created with cart details and items, redirecting users to the payment gateway for secure transactions.
- Upon successful purchase, an order object is generated, allowing admins to manage order status and track shipments effectively.
