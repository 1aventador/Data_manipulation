
  create or replace   view MY_TEST_PROJECT.dbt_schema.bronze_listings
  
  
  
  
  as (
    SELECT * FROM MY_TEST_PROJECT.staging.listings
  );

