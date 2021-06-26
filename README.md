# Bleeding-Hearts
The Child Opportunity Index (COI) is a measure used to determine the quality of both resources and conditions for children in their neighborhoods. This index takes into account 29 indicators and combines them into one single measurement tool to determine the overall “livability” of neighborhoods within the US. The 29 indicators are split up into 3 main domains: Education, Health and Environment, and Social and Economic. For example, the education domain looks at both the quality and access to early childhood education, quality of teachers, the number of children who attend high school, the number of students who take standardized tests, etc. All indicators listed within  each of the domains are measured at the census tract level. 

The ranking scale for COI ranges from 1 to 100, with 1 being the worst score and 100 being the highest score. Percentiles weighted using the total number of children in a given census tract are utilized in order to determine the cut off points for children living in the worst conditions and children living in the best conditions respectively. 

So why does the COI matter? According to Diversity Data Kids, children who live in neighborhoods with great early childhood education programs and schools, access to healthy food, clean air, steady shelter, and parks and playgrounds are more likely to become healthy and productive adults compared to children who don’t. The COI scores the general livability of neighborhoods throughout the United States by measuring the general accessibility and quality of resources necessary for children to develop well in their neighborhood of residence.

The American Community Survey (ACS) is a survey conducted by the U.S. Census Bureau that provides information about citizens and residents of the United States. According to the Census Bureau, ACS provides data on jobs, educational attainment, and other topics specifically to help policymakers assess the past, and, in doing so, design interventions.

We hypothesized that specific factors--such as data from the ACS-- that predict COI scores, with our focus on identifying factors that lead to low levels of child opportunity. This could be useful as a tool for policymakers to target effective public policy interventions in areas of low opportunity.

Using Random Forest and Gradient Boosting Classifiers that the following two features were most predictive of the child opportunity level: 

INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)_Families_Median family income (dollars)
INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)_With Food Stamp/SNAP benefits in the past 12 months

We found that SVC was the most effective model for our problem, and a next step for this project involves running feature imporance using SVC to confirm our findings using Random Fores and Gradient Boosting.

