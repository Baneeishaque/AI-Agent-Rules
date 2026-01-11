<!--
title: NestJS React App Rules
description: Guidelines for developing NestJS backends with React frontends.
category: Tech Stack
-->

# NestJS React App Rules

This document provides guidelines for the integration of NestJS backends with React frontends.

***

### 1. API Contract

- **OpenAPI**: Use Swagger/OpenAPI to document all endpoints.
- **Type Generation**: Generate TypeScript client types directly from the OpenAPI spec to ensure type safety.

### 2. Project Structure

- **Monorepo**: Prefer a monorepo structure (e.g., Nx or Turbo) for shared types and utilities.
