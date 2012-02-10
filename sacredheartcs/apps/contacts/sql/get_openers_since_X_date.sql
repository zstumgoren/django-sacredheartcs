select distinct(action_date) from contacts_emailaction order by 1 desc;

/* get distinct email addresses for all contacts who opened a message since X date */
select distinct(c.email_address)
from contacts_contact c 
join contacts_emailaction e on e.contact_id = c.id
where e.action_date > '2011-06-01'
order by c.email_address
;

/* count # of opens, by email address, since X date */
select c.email_address, count(e.action_date) "number_opened"
from contacts_contact c 
join contacts_emailaction e on e.contact_id = c.id
where e.action_date > '2011-06-01'
group by c.email_address
--order by c.email_address
order by 2 desc, 1
;