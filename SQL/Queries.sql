USE animalshelter;

-- Table of all adopted animals PES1UG20CS697
SELECT AName, CName FROM 
Customer natural join animal 
where SSN = AdoptedSSN;

-- Customers without phone numbers on the database using left outer join PES1UG20CS697
SELECT * FROM
Customer LEFT OUTER JOIN CustomerPhone on CustomerPhone.SSN = Customer.SSN
WHERE isNull(CustomerPhone.SSN);


-- Table of all animals died before adoption PES1UG20CS697
SELECT AName FROM
Animal
where !isNULL(EuthanizeEmployeeID) and isNULL(AdoptedSSN);

-- Total donations PES1UG20CS697
SELECT S.SName, sum(DAmount) as totalDonations FROM 
donations natural join Shelter as S
group by Shelterlicense;

-- Adoptions from shelter with most animals PES1UG20CS697
-- SELECT max(Count_) FROM (SELECT Shelterlicense as S, count(Shelterlicense) as Count_ FROM
-- Animal natural join Shelter
-- where LivesShelterLicense = ShelterLicense
-- group by Shelterlicense);

-- Adoptions from shelter with most animals PES1UG20CS697
with a (S, SName, Count_, AdoptCount) as
(select Shelterlicense, SName, count(Shelterlicense), count(AdoptedSSN)
from Animal natural join Shelter
where LivesShelterlicense = Shelterlicense group by Shelterlicense order by count(Shelterlicense) desc)
select S as Shelter, SName, max(a.Count_) as NoOfAnimals, AdoptCount as NoOfAdoptedAnimals
from a;

SELECT LivesShelterlicense, AdoptedSSN FROM
Shelter natural join Animal
where LivesShelterlicense = Shelterlicense;
-- group by LivesShelterlicense;

SELECT count(EmployeeID) from cares 
group by EmployeeID;