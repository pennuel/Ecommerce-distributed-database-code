# Ecommerce Distributed database Assignment

## the assignment question
create a distributed heterogeneous database environment
comprising three sites with three different participating database platforms,
and at least two different operating systems.
Use the above environment to demonstrate your
grasp of fragmentation and reconstruction. Think of a domain area comprising of
at least four distributed relations. Write out your applications/reports and
use them to perform fragmentation. Come up with appropriate query access
frequencies of your choice. Allocate the fragments by implementing them
physically in the participating databases. Choose one of the sites to be the
decision site and perform reconstruction using either views, functions, stored
procedures or any other technique.

## Approach
to create the environment, site used were a windows pc as the host for a VMware virtual machines and two Ubuntu virtual machines. 
Each computer was running as a Site.
The Ubuntu VMs were running PostgreSQL, and MariaDB while the Windows PC is running MySQL.
All three computers were placed in the same VLAN 192.168.52.0 where the VMware VMs were setup on a host-only network configuration.


The domain choosen was Ecommerce.
The create tables were customers table with customer information, product information, orders and payment.
To show fragmentation,
the customer tables was horizontally fragmented based on the customer country inthis case Nairobi and Mombase to create two tables
the products were vertically fragmented based on the product category, in this case electronics and clothing to create two tables.
the orders were horizontally fragmented based on the region to emulate that orders based on their location
then the payment was vertically fragmented based on the payment method in this case it was paypal and credit cards.

for the reconstruction, the python modules where used, were PostgreSQL i used psycogy2. For MariaDB and MySQL, I used pymsql to communicate with the databases.
The reports generated were:
1) Sales by payment_method per region
2) Customer order summary

it was heavy assignment but with GOOD problem solving skills it was finished.

#Modifications
i used python config module to create a config file for the database connection information.



