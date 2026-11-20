# AssetTrack demo development

This is an MIT-licensed adaptation of github-samples/contoso-inventory.
Use synthetic data only. The default demo branch is `demo-baseline`.

- Read the relevant service README and existing code before making changes.
- Keep each demo issue atomic and satisfy its acceptance criteria.
- Use .NET 10 for assets, Java 21 for workforce, Java 17 targets for auth/audit,
  Python 3.12 for reporting/notifications, and Astro/React for the web.
- Follow existing REST response shapes and service boundaries.
- Add focused regression tests for fixes and use parameterized database queries.
- Run `dotnet test services/assets-svc/Tests/AssetsService.Tests.csproj`,
  `mvn verify` in each changed Java service, and `npm run build` in services/web
  as relevant. Compile changed Python modules and exercise their endpoints in tests.
- The Java SQL injection examples are intentional security exercises. Fix them
  only when the selected issue or code scanning alert asks for it.
- Never use real credentials or deploy this intentionally insecure app publicly.
- Do not merge demo PRs or change another seeded scenario unless asked.
