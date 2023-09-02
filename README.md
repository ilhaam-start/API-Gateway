# Data Engineering in the Cloud

This is the final project for the Data Engineering Makers specialist track.

## Who you work for

You work for an organisation called Global Education Insights (GEI).

GEI is a non-profit organization dedicated to improving education systems
worldwide.

They work with governments, educational institutions, and other stakeholders to
provide data-driven insights and recommendations for educational policy and
practice.

Their mission is to ensure that every child has access to quality education,
regardless of their background or circumstances.


## Project overview

GEI has recently acquired the PISA 2018 dataset, a comprehensive survey of
student performance in various countries.

This dataset contains a wealth of information that can help GEI understand the
factors that contribute to student success and identify areas where education
systems can be improved.

However, the dataset is large and complex, making it difficult for GEI's team to
extract meaningful insights from it.

**That's where you come in.**

Your task is to leverage your data engineering skills to analyze the PISA 2018
dataset and develop a functioning dashboard that GEI can use to easily visualise
and interpret the data.

This dashboard will be a critical tool for GEI, helping them to make data-driven
decisions and recommendations.

The project will be carried out in a distributed environment in the Cloud, which
will allow for efficient data processing and collaboration among team members.


## Project objectives

The basic goal: you must get a dashboard showing, in as real-time as possible,
some calculations and metadata about a bunch of high-throughput application
databases.

Your coach will give you access to a dashboarding tool (Forage) which contains
several charts, which start simple, and get more complex in a variety of
open-ended ways.

> Each of you will have your own Forage account, so that you can track your
> progress individually.

You are given three levels of challenge:

- Level 1: Develop Forage charts displaying correct summary data that is no
   more than an hour old.
- Level 2: The same as Level 1, but the data should be no more than a minute
   old.
- Level 3: The same as Level 2, but the data should be up-to-the-second.

:information_source: The last level is a pretty insane task to achieve in only 1
week.


## Learning objectives

By the end of this project, you should be able to:

- Leverage your data engineering skills to create a real-time dashboard for an
  organization.
- Gain experience working in a distributed environment in the Cloud.


## Where to start

You can tackle charts them in any order, tackle them partially, spend the whole
time making one single chart work every second, or split the responsibilities
for tackling them among a team.

As part of this project, it's expected that you:

1. Do a data analysis on the country databases, figuring out what all the
   columns mean (with the help of the [resources](https://github.com/ilhaam-start/data-engineering-in-the-cloud/tree/7cbe9f3c50840ce13cd9e6e7bc40a4697172edd9/resources)), and how to
   handle the slightly messy data.
2. Retro-engineer the data structures needed to make the Forage charts work,
   with the help of the [specifications](https://github.com/ilhaam-start/data-engineering-in-the-cloud/tree/7cbe9f3c50840ce13cd9e6e7bc40a4697172edd9/specifications).

<!-- OMITTED -->

3. Construct an appropriate analytical database structure to supply the data,
   and make it available via a single, poll-able endpoint.
4. Figure out how to batch- or stream-process data from the application
   databases into their relevant analytical databases.
