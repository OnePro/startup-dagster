--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE IF EXISTS demo_db;

CREATE DATABASE demo_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';

\connect demo_db

DROP SCHEMA IF EXISTS public;
CREATE SCHEMA public;

CREATE TABLE public.demo_table (
    first_name text,
    last_name text
)
WITH (autovacuum_enabled='true', autovacuum_vacuum_scale_factor='0.01', autovacuum_analyze_scale_factor='0.005');