# DataOps Platform Comparison: Technical Capabilities Analysis

## Executive Summary

This comprehensive technical comparison evaluates Keboola, Microsoft Fabric, and Databricks across eight critical DataOps dimensions. **Databricks and Keboola demonstrate the most mature capabilities overall**, with Databricks excelling in open-source foundations and Keboola emphasizing automatic metadata capture. **Microsoft Fabric shows strong integration within the Azure ecosystem but has notable gaps in column-level lineage and native data quality frameworks**. All three platforms offer enterprise-grade capabilities with varying approaches to vendor lock-in.

## 1. Data Lineage Visualization

### Keboola: Industry-Leading Automatic Lineage
**Native capabilities: Comprehensive**

Keboola provides automatically-generated data lineage as a core platform feature with **no manual configuration required**. The system automatically captures operational metadata for every data operation, tracking datasets, buckets, columns, and dependencies from ingestion through transformation to output.

**Technical specifications:**
- **Column-level lineage**: YES - tracks individual column transformations and dependencies
- **Visual flow diagrams**: Native UI provides interactive visual representation across projects and teams
- **End-to-end traceability**: Complete tracking from source to consumption
- **OpenLineage integration**: Native support for OpenLineage standard, enabling export to external tools (Marquez, Collibra, Atlan)
- **Metadata scope**: 44+ telemetry tables capturing 1,100+ attributes covering jobs, flows, transformations, storage, users, and security events

**Unique advantage**: Impact analysis capabilities built-in to understand effects of schema changes and identify broken dependencies before they occur.

### Microsoft Fabric: Item-Level Focus with Limitations
**Native capabilities: Present but limited**

Microsoft Fabric provides lineage visualization through workspace lineage views and Microsoft Purview integration, but with significant constraints.

**Technical specifications:**
- **Column-level lineage**: NOT SUPPORTED for most Fabric items (only available for Power BI datasets)
- **Visual flow diagrams**: YES - interactive canvas showing relationships between workspace items
- **Cross-workspace lineage**: NOT SUPPORTED for non-Power BI items
- **Purview integration**: Extended capabilities through Microsoft Purview scanning for Datamart, Dashboard, Dataset, and Spark Job Definition

**Limitations**: Lineage functionality remains in preview status as of 2025, with external data sources as upstream sources not yet supported for non-Power BI items. Sub-item level lineage for Lakehouse tables and files is not available.

### Databricks: Comprehensive Unity Catalog Lineage
**Native capabilities: Comprehensive**

Databricks Unity Catalog provides automatic runtime data lineage with **column-level granularity** across all supported languages (SQL, Python, R, Scala).

**Technical specifications:**
- **Column-level lineage**: YES - automatic tracking down to individual columns
- **Visual flow diagrams**: Interactive lineage graphs in Catalog Explorer showing table-to-table and column-to-column relationships
- **Real-time capture**: Runtime lineage captured automatically across all queries
- **API access**: REST API and lineage system tables for programmatic access and integration with external tools
- **External asset support**: Can include workflows run outside Databricks (Public Preview)

**Requirements**: Requires Unity Catalog enablement and Databricks Runtime 11.3 LTS+ for streaming lineage, 13.3 LTS+ for column lineage in Delta Live Tables pipelines.

### Comparative Assessment
**Winner**: Keboola and Databricks tie for most comprehensive lineage capabilities. Keboola's automatic capture with OpenLineage standard support provides excellent interoperability, while Databricks offers native column-level tracking with powerful visual tools. **Microsoft Fabric lags significantly** with item-level-only lineage for most data assets.

---

## 2. Built-in Data Quality Tests

### Keboola: Flexible Template-Based Framework
**Native capabilities: Comprehensive**

Keboola provides data quality testing through a template-based framework with SQL procedures and custom code support.

**Technical specifications:**
- **Data Quality template**: Pre-built Snowflake SQL procedures with unified DQ_RESULTS_LOG table for centralized test results
- **Test types**: Completeness (missing data, nulls), uniqueness (duplicates), validity (thresholds, outliers), consistency (schema validation), accuracy (business rules)
- **Custom testing**: Write tests in SQL, Python, R, or Julia within transformations; 27+ example SQL checks available
- **Automation**: Tests orchestrated automatically within data pipelines via Flows
- **Actions on failure**: Conditional ABORT transformation to stop processing, alerts via Slack/email, or automated healing scripts

**Limitation**: No standalone native UI for defining quality rules; requires SQL/Python knowledge for custom tests.

### Microsoft Fabric: Limited Native Framework
**Native capabilities: Minimal**

Microsoft Fabric lacks a comprehensive built-in data quality framework, requiring third-party tools or custom implementations.

**Available approaches:**
- **DataFlow Gen2**: Visual transformations with basic filter transformations for null checks
- **Great Expectations integration**: Recommended third-party Python library requiring manual setup as a public library in Fabric Environment
- **Microsoft Purview Data Quality** (preview): No-code/low-code rules with AI-powered profiling and quality scoring
- **Custom implementations**: Validation via Notebooks using Python or pipeline conditional logic

**Critical gap**: No comprehensive native framework comparable to competitors. Organizations must implement custom solutions or rely on external tools.

### Databricks: Delta Live Tables Expectations
**Native capabilities: Comprehensive within DLT**

Databricks provides data quality capabilities primarily through **Delta Live Tables (DLT) Expectations**, a declarative framework for defining data quality constraints.

**Technical specifications:**
- **Three violation modes**:
  - `expect`: Retain invalid records but track metrics
  - `expect_or_drop`: Drop records violating constraints
  - `expect_or_fail`: Fail pipeline on constraint violations
- **Schema validation**: Automatic schema enforcement and evolution via Delta Lake
- **Quality monitoring**: Automatic logging to event logs stored as Delta tables
- **Quality metrics dashboard**: Built-in UI showing data quality metrics
- **Quarantine support**: Separate storage for invalid data for review

**Example implementation**:
```python
@dlt.expect("valid_timestamp", "timestamp > '2012-01-01'")
@dlt.expect_or_drop("valid_current_page", "current_page_id IS NOT NULL")
@dlt.expect_or_fail("critical_validation", "amount > 0")
```

**Limitation**: DLT expectations work exclusively with streaming tables and materialized views. No standalone data quality framework outside DLT pipelines.

### Comparative Assessment
**Winner**: Databricks offers the most mature native framework through DLT Expectations with built-in monitoring and dashboards. Keboola provides strong flexibility with template-based testing across any transformation. **Microsoft Fabric significantly lacks** native capabilities, requiring external tool integration.

---

## 3. Metadata Management

### Keboola: Active Metadata Architecture
**Native capabilities: Comprehensive with automatic capture**

Keboola's "Active Metadata" layer provides integrated metadata management embedded natively in the platform with **zero manual maintenance**.

**Technical specifications:**
- **Automatic schema detection**: YES - Storage component automatically detects and manages schemas with evolution tracking
- **Data cataloging**: Native Data Catalog for certifying datasets as data products with metadata enrichment
- **Business glossary/tagging**: Custom key-value tags applied to tables, buckets, flows, and configurations; tag-based governance policies
- **Metadata capture**: 44+ telemetry tables automatically populated with 1,100+ attributes covering:
  - Operational metadata: jobs, flows, transformations
  - Technical metadata: storage, schemas, data types
  - Usage metadata: users, access patterns, adoption metrics
  - Cost metadata: credit consumption per job/team
  - Security metadata: 50+ event types (logins, token creation, role changes)

**Architecture**: Structured at organization, project, and branch levels with API-first design. All metadata accessible via REST API and native GraphQL endpoint.

### Microsoft Fabric: Purview-Centric Approach
**Native capabilities: Comprehensive via integration**

Microsoft Fabric provides metadata management through tight integration with **Microsoft Purview**, attached by default to every Fabric instance.

**Technical specifications:**
- **Automatic schema detection**: YES - Delta tables with schema evolution support
- **Data cataloging**: Unified Catalog with live view of Fabric items, browse and search without requiring data access permissions
- **Business glossary**: Available through Purview
- **Tagging**: Sensitivity labels, classifications, data product associations
- **Schema Registry**: Available for Eventstreams with Avro schema validation
- **OneLake Catalog**: Category behavior for organizing and filtering items

**Purview features**: Data Map automatically scans and catalogs Fabric items with column-level metadata for certain item types, data quality profiling, and lineage visualization. Supports Lakehouse, Warehouse, Data Pipeline, Dataflow Gen2, KQL Database, Eventstream, Power BI artifacts, Notebooks, Spark Job Definitions, ML Models, and SQL Database (preview).

**Configuration**: Metadata scanning configured via Admin portal with service principal authentication support and cross-geo metadata access.

### Databricks: Unity Catalog Foundation
**Native capabilities: Comprehensive with recent open-sourcing**

Databricks Unity Catalog provides centralized metadata management across all data assets with a **three-level hierarchy** (Metastore → Catalogs → Schemas → Objects).

**Technical specifications:**
- **Automatic schema detection**: YES - for data ingestion
- **Data cataloging**: Centralized repository for all data assets with Catalog Explorer UI
- **Business glossary**: Limited native support; organizations typically integrate with Microsoft Purview, Atlan, Collibra, or Alation
- **Tagging**: Custom tags, data classification, sensitivity labels
- **Access control**: Fine-grained security at catalog, schema, table, column, and row levels
- **Metadata features**: System tables for audit logs, billable usage, lineage data; ownership tracking; schema evolution tracking

**Critical development**: Unity Catalog **open-sourced in June 2024**, enabling wider adoption beyond Databricks. Supports multiple table formats: Delta Lake, Apache Iceberg, Apache Hudi, Parquet.

**Limitation**: Unity Catalog focuses on technical metadata; business metadata and glossary capabilities often require complementary third-party tools.

### Comparative Assessment
**Winner**: Keboola provides the most automatic metadata capture with no manual configuration. Microsoft Fabric offers the most comprehensive business glossary through Purview integration. Databricks Unity Catalog excels in technical metadata and governance with recent open-sourcing improving portability. All three provide enterprise-grade capabilities with different architectural approaches.

---

## 4. Git Integration

### Keboola: CLI-Based "Keboola as Code"
**Native capabilities: Comprehensive via CLI**

Keboola provides Git integration through its CLI tool, representing the entire project as a local directory structure with JSON configuration files.

**Technical specifications:**
- **CLI commands**: `kbc init` (initialize and pull), `kbc pull` (sync from Keboola), `kbc push` (deploy to Keboola), `kbc diff` (compare states), `kbc persist` (copy configurations)
- **Git providers**: Works with GitHub, Bitbucket, GitLab, and any Git server
- **Branching**: Native Keboola branches (GUI-based virtual branches) can be mapped to Git branches
- **GitHub Actions**: Pre-built workflows for automated sync, validation (dry-run), and CI/CD pipeline integration
- **Multi-environment support**: DEV/TEST/PROD lifecycle via Git with `--allow-target-env` mode for GitOps frameworks

**Collaboration**: Multi-stage environment management, multi-project architecture support, template deployment from Git repositories, code review through Git pull requests.

**Limitation**: Not a native GUI-based Git integration; requires CLI installation and Git knowledge. Branches cannot be created locally (must be created in GUI first).

### Microsoft Fabric: Native Workspace Integration
**Native capabilities: Comprehensive with provider-specific support**

Microsoft Fabric provides **native Git integration** at the workspace level with visual Git client built into the UI.

**Technical specifications:**
- **Supported providers**: Azure DevOps (recommended - full features), GitHub (cloud), GitHub Enterprise (cloud with limitations)
- **Core features**: Workspace-level connection to Git repositories and branches, full branching/committing/merging, bi-directional sync (commit to Git, update from Git), branch out (create new branches with associated workspaces)
- **Authentication**: OAuth credentials (recommended), Personal Access Tokens, fine-grained tokens; service principal NOT supported for Git operations
- **Supported items**: Extensive coverage including Environment, Lakehouse, Notebooks, Spark Job Definitions, Data Pipeline, Dataflow Gen2, Eventstream, Eventhouse, KQL Database, Warehouse, Power BI Reports/Semantic Models, SQL Database

**Technical limits**: 
- Commit size: 125 MB (25 MB for Azure DevOps)
- Branch name: 244 characters max
- File path: 250 characters max
- File size: 25 MB
- Folder depth: Up to 10 levels

**Limitations**: Only workspace admins can manage Git connections; MyWorkspace cannot connect; submodules not supported; sovereign clouds not supported.

### Databricks: Native Repos/Git Folders
**Native capabilities: Comprehensive visual Git client**

Databricks provides native Git integration through **Databricks Git Folders** (formerly Repos) with a built-in visual Git client.

**Technical specifications:**
- **Supported providers**: GitHub (Cloud and Enterprise), GitLab, Bitbucket, Azure DevOps, AWS CodeCommit, self-hosted Git servers
- **Git operations**: Clone repositories, commit and push changes, pull remote changes, branch management (create, switch, merge, rebase), visual diff comparison, conflict resolution UI, sparse checkout support
- **Authentication**: OAuth credentials (recommended), Personal Access Tokens, service principal support for CI/CD
- **CI/CD integration**: Repos REST API for programmatic updates, GitHub Actions integration, automated pipeline updates, scheduled workflows

**Collaboration features**: Personal development branches per user, feature branch workflows, pull request creation from Databricks UI, shared production folders managed by admins.

**Limitation**: Designed primarily for notebooks and Python/Scala/R files; not all Git operations available via UI (some require CLI); complex merge scenarios may need external Git client.

### Comparative Assessment
**Winner**: Microsoft Fabric and Databricks both offer superior **native GUI-based Git integration** with visual clients and comprehensive provider support. Keboola's CLI-based approach is powerful for GitOps workflows but requires more technical expertise. Microsoft Fabric has the best Azure DevOps integration, while Databricks supports the widest range of Git providers including self-hosted servers.

---

## 5. API/CLI Quality

### Keboola: API-First Architecture
**Native capabilities: Excellent - comprehensive suite**

Keboola follows an **API-first design** where everything in the UI is accessible via API.

**Technical specifications:**
- **REST APIs**: All components have public APIs documented on Apiary (keboola.docs.apiary.io)
  - Storage API (core data management)
  - Docker Runner API (component execution)
  - Transformations API (SQL, Python, R)
  - Orchestrator/Scheduler API (workflow automation)
  - Management API (project and organization management)
  - Queue API, Encryption API, Sandboxes/Workspaces API
- **Multi-region support**: APIs available across AWS, Azure, GCP stacks with service discovery via API Index
- **Python SDKs**: Three official libraries
  - `sapi-python-client`: Tables, buckets, files operations
  - `keboola.component`: Wrapper for Common Interface with config manipulation
  - `keboola.http-client`: Built-in retry mechanism and error handling
- **CLI tools**: 
  - **Keboola CLI (kbc)**: Full project management with init, pull, push, diff operations
  - **Storage API CLI**: Docker-based CLI for table/bucket operations

**Documentation quality**: Interactive Apiary console with code examples in multiple languages, Postman collections, comprehensive developer documentation site (developers.keboola.com).

### Microsoft Fabric: Comprehensive Multi-Tool Approach
**Native capabilities: Comprehensive**

Microsoft Fabric provides extensive programmatic access through REST APIs, multiple SDKs, and CLI tools.

**Technical specifications:**
- **REST APIs**: Comprehensive Microsoft Fabric REST API covering Core (workspaces, items, capacities), Admin (tenant settings, monitoring), and workload-specific operations
  - CRUD operations for all artifacts
  - Job scheduler APIs (run, cancel, status)
  - Git integration APIs (commit, update, connect)
  - Deployment pipeline APIs
- **Python SDKs**: 
  - **Official SDK**: `microsoft-fabric-api` on PyPI with Azure Identity authentication
  - **Community SDK**: `msfabricpysdkcore` (wrapper around REST APIs v1)
  - **FabricFlow**: Community SDK for pipelines and automation
  - **SemPy**: Microsoft's library for Fabric notebooks with built-in token management
- **CLI tools**:
  - **Fabric CLI (`fab`)**: Official command-line interface with file-system-inspired navigation (ls, cd, mkdir, cp, rm, run)
  - **OneLake PowerShell**: Azure Storage PowerShell module integration (`Az.Storage`)
  - **FabricTools**: Community PowerShell module for workspace management

**Authentication**: Service Principal (limited support - mainly Admin and Core APIs), user authentication (delegated permissions), Azure CLI authentication, OAuth tokens, Managed Identity.

**Limitation**: Service principal not supported for all API operations; Lakehouse APIs have limitations; rate limiting applies.

### Databricks: Enterprise-Grade API Suite
**Native capabilities: Excellent - comprehensive coverage**

Databricks provides a complete REST API with multiple SDKs and CLI options.

**Technical specifications:**
- **REST API**: Complete API version 2.0 covering all Databricks operations
  - Workspace management, cluster operations, jobs orchestration, Repos management
  - Unity Catalog operations, SQL warehouses, MLflow operations
  - OpenAPI/Swagger documentation
- **Python SDK**: Official `databricks-sdk` 
  - Auto-generated from OpenAPI specs with Pythonic interface
  - Type hints and IDE support, async support
  - Example: `client.lineage.get_table_lineage(catalog_name, schema_name, table_name)`
- **Additional SDKs**: Java SDK, Go SDK, official Terraform provider
- **CLI tools**: 
  - **Databricks CLI**: Command-line interface wrapping REST API with native commands for common operations
  - Generic API access: `databricks api get/post` for any REST endpoint
  - Multi-profile authentication support

**API quality**: Comprehensive coverage, well-documented, consistent RESTful design, active maintenance.

**Considerations**: Some preview features have changing APIs; complex operations may require multiple API calls; rate limiting on some endpoints.

### Comparative Assessment
**Winner**: All three platforms offer **excellent API/CLI quality**. Keboola's API-first design ensures 100% UI functionality is accessible programmatically. Microsoft Fabric provides the most diverse tooling with PowerShell integration for Windows-centric environments. Databricks offers the most mature SDKs with auto-generated code and comprehensive type support.

---

## 6. Automated Testing

### Keboola: Multi-Level Testing Framework
**Native capabilities: Comprehensive with CLI support**

Keboola provides testing capabilities at template, component, and data pipeline levels.

**Technical specifications:**
- **Template testing**: `kbc template test create` and `kbc template test run` commands with expected output validation and wildcard assertions
- **Component testing**: Docker-based testing, Debug API for local development, Run Tag API for unreleased images, PHPUnit integration, Travis CI integration
- **Data pipeline testing**: ETL/ELT testing within transformations, regression testing for schema changes, end-to-end integration testing
- **Test types**: Unit tests (component-level), integration tests (cross-component), data quality tests (automated validation)
- **CI/CD integration**: GitHub Actions workflows with validate workflow (`push --dry-run`), automated testing before deployment, CLI validation commands

**Best practices**: Test data generation via Python transformations, shared code libraries for reusable tests, result logging to DQ_RESULTS_LOG table.

**Limitation**: No standalone native testing UI; requires technical knowledge; manual test creation for custom components.

### Microsoft Fabric: Framework Support via CI/CD
**Native capabilities: Moderate - requires external CI/CD tools**

Microsoft Fabric supports automated testing through CI/CD integration rather than native testing framework.

**Technical specifications:**
- **Testing approaches**:
  - Deployment Pipelines: Native Fabric tool for Dev/Test/Prod staging
  - Git integration + Azure DevOps: Automated testing in release pipelines
  - GitHub Actions: Workflow automation with testing stages
- **Testing frameworks**:
  - **Data Factory Testing Framework**: Open-source Python framework (`data-factory-testing-framework`) for pipeline and dataflow unit tests
  - **PyTest integration**: Standard Python testing with pytest in CI/CD pipelines
  - **Great Expectations**: Data validation testing with expectation suites
- **CI/CD patterns**: Git → Build → Test → Deploy with PR triggers, automated tests in build environment, deployment to staging, post-deployment validation
- **fabric-cicd**: Community Python library for automated deployment to multiple workspaces with Azure DevOps integration

**Test capabilities**: Unit tests (pipeline activities, notebook code), integration tests (end-to-end validation), data quality tests (Great Expectations), post-deployment tests.

**Limitations**: No native comprehensive testing framework; requires external CI/CD tools (Azure DevOps, GitHub Actions); manual setup of test infrastructure; service principal configuration required.

### Databricks: Standard Framework Integration
**Native capabilities: Strong framework support**

Databricks supports automated testing through standard testing frameworks with native integration.

**Technical specifications:**
- **Supported frameworks**: 
  - Python: pytest, unittest (built-in)
  - R: testthat
  - Scala: ScalaTest
  - SQL: Custom test queries
- **Implementation patterns**:
  - In-notebook testing with unittest
  - Separate test notebooks using `%run` to import functions
  - External test files in Python modules via Git folders
- **Integration testing**: DLT pipeline testing via expectations, job orchestration testing, MLflow integration for tracking test results
- **CI/CD integration**: GitHub Actions for running tests on commits, Azure DevOps pipeline support, API-driven test execution, scheduled notebook runs

**Test organization**: Module-based development with pytest, driver notebooks for test orchestration, separate test notebooks for Scala.

**Third-party tools**: `databricks_test` (community open-source framework), partner testing platforms (e.g., Datagaps).

**Limitations**: No native dedicated testing framework; notebook-based testing has limitations; coverage reporting requires additional setup; integration testing more complex than unit testing.

### Comparative Assessment
**Winner**: Keboola provides the most integrated testing approach with CLI-based template and component testing. Databricks offers the strongest support for standard testing frameworks (pytest, unittest) with MLflow integration. **Microsoft Fabric requires the most manual setup** and external tool dependencies. All three platforms support CI/CD integration but require technical implementation effort.

---

## 7. Documentation Quality

### Keboola: Dual-Site Documentation Strategy
**Assessment: Excellent - clear audience separation**

Keboola maintains two comprehensive documentation sites targeted at different audiences.

**Structure:**
- **User Documentation** (help.keboola.com): End users, analysts, data engineers
  - 6-part Getting Started tutorial series (loading data, manipulation, writing, automation, analysis, branches)
  - Components, transformations, flows, storage, development branches
  - Templates, management & security, best practices, governance guide
- **Developer Documentation** (developers.keboola.com): Component developers, API users, DevOps
  - API references, CLI docs, integration guides
  - Component development, template creation, Common Interface specs

**Additional resources:**
- Keboola Academy learning modules
- Technical blog (keboola.com/blog) and tech blog (500.keboola.com)
- 600+ GitHub repositories with README files
- Changelog (changelog.keboola.com) and status page
- Support via email and in-project forms

**Strengths**: Clear separation between user and developer docs, comprehensive feature coverage, practical hands-on tutorials, active maintenance, searchable interface with visual diagrams.

**Limitations**: No single unified search across both doc sites; some advanced features require multiple doc pages; legacy wiki content being phased out.

### Microsoft Fabric: Comprehensive Microsoft Learn Integration
**Assessment: Comprehensive and high quality**

Microsoft Fabric leverages the extensive Microsoft Learn platform for documentation.

**Coverage:**
- **Fundamentals**: Platform overview, architecture, getting started, core concepts (OneLake, workspaces, capacities)
- **Workload-specific docs**: Data Engineering, Data Factory, Data Warehouse, Real-time Intelligence, Data Science, Power BI integration
- **Developer documentation**: REST API references, SDK documentation, Git integration, CI/CD workflows, notebook APIs
- **Administration**: Tenant settings, security and governance, capacity management, monitoring
- **Tutorials & learning paths**: Microsoft Learn training modules, hands-on labs, video tutorials (Data Exposed series)

**Additional resources:**
- Monthly feature summaries on Microsoft Fabric Blog
- Release plan documentation with roadmap
- Microsoft Fabric Community forums
- Certifications: DP-600 (Fabric Analytics Engineer Associate - GA), DP-700 (Fabric Data Engineer - Beta)

**Strengths**: Frequent updates (monthly feature releases documented), code samples included, clear prerequisites and step-by-step instructions, architecture diagrams, limitations clearly documented, feedback mechanism on every page.

**Gaps**: Platform evolving rapidly (preview features change frequently), some community-reported gaps between documentation and actual behavior, preview features may have incomplete documentation.

### Databricks: Multi-Tier Learning Ecosystem
**Assessment: Comprehensive with strong training focus**

Databricks provides extensive documentation complemented by a robust training and certification program.

**Official documentation** (docs.databricks.com):
- Platform-specific docs (AWS, Azure, GCP)
- Persona-based sections (Data Engineering, ML, SQL)
- API reference documentation, tutorials, best practices

**Databricks Academy** (FREE):
- Role-based learning paths
- On-demand video courses and hands-on labs
- Instructor-led training options
- Certification programs: Data Engineer (Associate, Professional), Machine Learning, SQL Analytics
- Courses covering fundamentals, pipelines, ML workflows, Delta Lake, Unity Catalog, optimization

**Additional resources:**
- Databricks Community forums and MVP program
- GitHub repositories with examples and demos
- dbdemos (automated demo installer)
- Third-party courses: DataCamp, Coursera/edX, Udemy
- Conference talks (Data + AI Summit)

**Strengths**: Comprehensive and well-organized, multi-cloud coverage, regular updates, active community, free training access, real-world examples.

**Enhancement areas**: Some advanced topics could be more detailed, preview features documentation sometimes sparse, more troubleshooting examples needed.

### Comparative Assessment
**Winner**: All three platforms provide **excellent documentation quality**. Microsoft Fabric benefits from Microsoft's extensive Learn platform and monthly updates. Databricks excels with free Academy training and certification programs. Keboola's dual-site strategy provides the clearest audience separation. For academic research, all three offer sufficient documentation depth.

---

## 8. Vendor Lock-In Analysis

### Keboola: Designed for Portability
**Assessment: Low vendor lock-in risk**

Keboola is architecturally designed to minimize lock-in by positioning as a layer **on top of** customer infrastructure.

**Open standards support:**
- **OpenLineage**: Native support for OpenLineage protocol with automatic telemetry export
- **Common Interface**: Standardized Docker-based component architecture with JSON configuration
- **Standard formats**: CSV for data import/export, JSON for configurations, standard SQL/Python/R for transformations

**Cloud agnosticism:**
- **Bring Your Own Database (BYOD)**: Works with Snowflake, BigQuery, Redshift, Synapse, Teradata
- Multi-cloud support: AWS, Azure, GCP
- **Critical architectural principle**: Data resides in YOUR warehouse, not Keboola systems
- Storage is customer's chosen warehouse

**Data export/portability:**
- **Data Takeout**: Get all project data back
- Storage API for programmatic data access
- All data exportable via APIs
- Table snapshots for version control
- No proprietary data formats

**Lock-in risk analysis:**

**LOW RISK factors:**
- Platform operates on customer infrastructure
- Data stays in customer warehouse
- Transformations use standard SQL/Python/R
- API-first design enables migration
- Configuration as code (JSON files)
- Git-based project definitions

**MODERATE RISK factors:**
- Flows (orchestration) specific to Keboola
- Some proprietary components
- Template format is Keboola-specific

**Migration strategy**: Configurations exportable as JSON, data already in customer warehouse, transformations are portable code, CLI enables bulk export.

**Keboola's design principle**: "No data is locked" - official commitment to avoiding technological dependencies that hurt agility.

### Microsoft Fabric: Open Format with Ecosystem Dependency
**Assessment: Moderate vendor lock-in**

Microsoft Fabric uses open standards for data storage but creates dependencies through Azure ecosystem integration.

**Open standards & formats:**
- **Delta Lake format**: Primary storage format (open-source Apache project)
  - Apache Parquet files with transaction log
  - ACID transaction support
  - Compatible with any Delta Lake-compatible engine
- **Apache Spark**: Open-source processing engine
- **SQL Standard**: T-SQL compatibility (SQL Server/Azure SQL alignment)

**Data portability features:**
- **Export capabilities**: SqlPackage command-line tool for database portability (.bacpac, .dacpac)
- **Shortcuts**: Reference data in external locations (ADLS Gen2, S3) without copying
- **OneLake File APIs**: Compatible with ADLS Gen2 APIs and SDKs
- **Standard formats**: Parquet (recommended), Delta, CSV, JSON, Avro, ORC
- **Cross-platform compatibility**: Shortcuts to AWS S3, compatible with Azure Databricks, Trino-based platforms can read Delta

**Azure ecosystem considerations:**

**Potential lock-in factors:**
1. **OneLake architecture**: Single OneLake per tenant with tight Azure integration
2. **Capacity-based licensing**: Fabric capacity tied to Azure subscription
3. **Microsoft Entra authentication**: Primary authentication method
4. **Power BI integration**: Deep integration with Microsoft BI stack
5. **Purview dependency**: Governance features rely on Microsoft Purview
6. **Azure services optimization**: Optimized for Azure infrastructure

**Mitigation strategies:**
- Open format foundation (Delta Lake) ensures data accessibility
- Shortcuts avoid data duplication
- Standard APIs (REST, SQL endpoints)
- Export tools (SqlPackage, APIs)
- Multi-cloud shortcuts support

**Lock-in assessment by layer:**
- **Data layer**: LOW (open formats)
- **Compute layer**: MODERATE (Spark is portable, but Fabric-specific features)
- **Metadata/governance**: HIGH (Purview-dependent)
- **Authentication**: MODERATE (Microsoft Entra ID centric)
- **Overall**: MODERATE - Data is portable, but platform features create ecosystem dependency

### Databricks: Open-Source Foundation with Proprietary Optimizations
**Assessment: Low to moderate vendor lock-in**

Databricks presents the most nuanced picture, with strong open-source foundations but some proprietary performance optimizations.

**Open-source foundations (LOW LOCK-IN):**

**Apache Spark Core:**
- Databricks built on 100% open-source Apache Spark
- Standard Spark APIs work identically
- **Code portability**: PySpark, Scala, R, SQL code can run on:
  - AWS EMR, Google Cloud Dataproc, Azure HDInsight
  - Open-source Spark clusters
  - Competitor platforms (Cloudera, etc.)

**Delta Lake - Fully Open Source (Critical Development):**
- **Delta Lake 2.0 fully open-sourced** in June 2022 (previously had proprietary features)
- Donated to Linux Foundation
- **Data format**: Parquet-based (open), Delta transaction logs are JSON (open)
- **Data stored in customer's cloud storage** (S3, ADLS, GCS)
- **Critical point**: You own the data, not locked in Databricks systems
- Compatible with Apache Flink, Presto/Trino, Apache Hive
- Delta Rust for non-JVM languages

**Recent open-sourcing efforts:**
- **Unity Catalog open-sourced June 2024** - Major strategic move
- Core governance features now open-source
- Demonstrates commitment to reducing lock-in

**Data portability (STRONG):**
- Data stored in YOUR cloud storage
- Standard cloud storage APIs
- Open formats (Delta/Parquet)
- No proprietary data format lock-in
- **Delta Sharing**: Open protocol for data sharing (read shared data without Databricks)
- **Universal Format (UniForm)**: Read Delta tables as Iceberg or Hudi

**Code portability (MODERATE TO HIGH):**

**Highly portable:**
- Standard Spark SQL
- PySpark, Scala Spark, R SparkR code
- Python UDFs
- SQL queries

**Less portable (Databricks-specific):**
- `dbutils` utilities (Databricks-specific)
- Databricks widgets
- Notebook magic commands (`%run`, `%sql`)
- MLflow (though open-source, some features Databricks-enhanced)
- **Mitigation**: Most Databricks-specific code can be abstracted or refactored

**Proprietary components (MODERATE LOCK-IN RISK):**

**Unity Catalog:**
- Open-sourced June 2024, but some advanced features may remain proprietary
- Metadata and governance model creates dependency
- Mitigation: Standard catalog APIs, metadata can be migrated

**Databricks Runtime:**
- Proprietary optimizations on top of Spark
- **Photon Engine**: Proprietary vectorized query engine with significant performance improvements
- **Lock-in consideration**: Code runs faster on Databricks, may be slower elsewhere
- **Mitigation**: Code still runs on standard Spark, just potentially slower

**Delta Live Tables (DLT):**
- **Proprietary framework** (not open-source)
- DLT syntax and patterns specific to Databricks
- **Mitigation**: Underlying Delta tables portable, pipelines need rewriting

**Migration analysis:**

**Migrating TO Databricks**: Easy to Moderate
- Standard Spark code works immediately
- Lift-and-shift from EMR/Dataproc straightforward
- Unity Catalog can connect to external metastores

**Migrating FROM Databricks**: Moderate
- **Data**: Very easy (already in your cloud storage, open formats)
- **Spark Code**: Easy (standard Spark APIs portable)
- **DLT Pipelines**: Requires rewrite for other orchestrators
- **dbutils Code**: Requires refactoring
- **Unity Catalog Metadata**: Exportable, requires mapping
- **Optimizations**: Performance tuning may need revisiting

**Vendor lock-in scoring:**
- **Low lock-in areas (80% of platform)**: Data storage/formats, core Spark processing, standard SQL, Delta Lake, APIs
- **Moderate lock-in areas (15%)**: Unity Catalog adoption, Databricks Runtime optimizations, MLflow managed services
- **Higher lock-in areas (5%)**: Delta Live Tables, Photon engine performance

**Critical competitive advantage**: Unlike traditional data warehouses (Snowflake, BigQuery, Redshift), Databricks built on open-source Apache Spark and open Delta format provides **fundamentally more portability**.

### Comparative Assessment
**Winner for Lowest Lock-In**: **Keboola** has the lowest vendor lock-in risk due to architectural design placing the platform on top of customer infrastructure with data residing in customer-chosen warehouses. **Databricks** demonstrates strong commitment to openness through recent open-sourcing of Delta Lake and Unity Catalog, providing excellent data and code portability. **Microsoft Fabric** has moderate lock-in primarily through Azure ecosystem dependencies and Purview-centric governance, though data portability via Delta Lake remains strong.

---

## Summary Comparison Matrix

| Dimension | Keboola | Microsoft Fabric | Databricks |
|-----------|---------|------------------|------------|
| **Data Lineage** | ⭐⭐⭐⭐⭐ Native, automatic, column-level, OpenLineage | ⭐⭐⭐ Item-level only (NO column-level) | ⭐⭐⭐⭐⭐ Native, automatic, column-level |
| **Data Quality Tests** | ⭐⭐⭐⭐ Template-based, flexible, SQL/Python | ⭐⭐ Limited native, requires Great Expectations | ⭐⭐⭐⭐⭐ DLT Expectations, comprehensive |
| **Metadata Management** | ⭐⭐⭐⭐⭐ Automatic capture, 1,100+ attributes | ⭐⭐⭐⭐⭐ Purview integration, comprehensive | ⭐⭐⭐⭐⭐ Unity Catalog, open-sourced 2024 |
| **Git Integration** | ⭐⭐⭐⭐ CLI-based, comprehensive | ⭐⭐⭐⭐⭐ Native GUI, Azure DevOps optimized | ⭐⭐⭐⭐⭐ Native GUI, multi-provider |
| **API/CLI Quality** | ⭐⭐⭐⭐⭐ API-first design, comprehensive | ⭐⭐⭐⭐⭐ Excellent, multi-tool approach | ⭐⭐⭐⭐⭐ Excellent, mature SDKs |
| **Automated Testing** | ⭐⭐⭐⭐ Multi-level framework, CLI support | ⭐⭐⭐ Requires external CI/CD setup | ⭐⭐⭐⭐ Standard framework support |
| **Documentation** | ⭐⭐⭐⭐⭐ Dual-site strategy, clear separation | ⭐⭐⭐⭐⭐ Microsoft Learn, comprehensive | ⭐⭐⭐⭐⭐ Excellent with Academy training |
| **Vendor Lock-In** | ⭐⭐⭐⭐⭐ LOWEST - Data in your warehouse | ⭐⭐⭐ MODERATE - Azure ecosystem dependency | ⭐⭐⭐⭐ LOW-MODERATE - Open-source foundation |

## Key Findings for Master's Thesis

### Platform Positioning

**Keboola** positions as a **DataOps orchestration layer** that sits on top of customer infrastructure, emphasizing zero vendor lock-in and automatic metadata capture. Best suited for organizations requiring multi-cloud flexibility and those with existing data warehouse investments.

**Microsoft Fabric** represents Microsoft's **unified analytics platform** deeply integrated with Azure ecosystem and Power BI. Best suited for organizations already invested in Microsoft/Azure technology stacks and requiring tight integration with enterprise Microsoft services.

**Databricks** positions as a **lakehouse platform** built on open-source foundations (Spark, Delta Lake) with proprietary performance optimizations. Best suited for organizations requiring advanced analytics, machine learning capabilities, and open-source portability with enterprise features.

### Critical Differentiators

1. **Column-level lineage**: Keboola and Databricks provide comprehensive column-level lineage automatically; Microsoft Fabric does NOT support column-level lineage for most items (major gap)

2. **Data quality frameworks**: Databricks DLT Expectations offers the most mature native framework; Microsoft Fabric requires third-party tools (significant weakness)

3. **Vendor lock-in**: Keboola has lowest lock-in (data in customer warehouse); Databricks has strong portability (open-source Spark/Delta Lake); Microsoft Fabric has moderate lock-in (Azure ecosystem dependency)

4. **Git integration**: Microsoft Fabric and Databricks provide superior native GUI-based Git integration; Keboola requires CLI expertise

5. **Metadata automation**: Keboola automatically captures 1,100+ attributes with zero configuration; others require more setup

### Academic Considerations

For a master's thesis comparing DataOps platforms, emphasize these analytical dimensions:

- **Architectural philosophy**: Keboola (orchestration layer), Fabric (unified platform), Databricks (lakehouse)
- **Open vs. proprietary**: Databricks leads in open-source commitment, recently open-sourcing Delta Lake and Unity Catalog
- **Integration strategy**: Fabric excels in Microsoft ecosystem integration; Keboola emphasizes BYOD approach
- **Data portability**: Keboola and Databricks prioritize portability through architecture and open formats; Fabric achieves data portability through Delta Lake but creates platform dependencies
- **Maturity assessment**: Keboola (established DataOps), Databricks (mature lakehouse), Fabric (evolving unified platform with many preview features as of 2025)

### Recommendations for Platform Selection

**Choose Keboola if:**
- Requiring maximum vendor lock-in avoidance
- Already have preferred data warehouse (Snowflake, BigQuery, Redshift)
- Need automatic metadata capture without configuration
- Prioritize multi-cloud flexibility

**Choose Microsoft Fabric if:**
- Already invested in Azure/Microsoft ecosystem
- Require tight Power BI integration
- Need unified platform for all analytics workloads
- Accept moderate Azure ecosystem dependency

**Choose Databricks if:**
- Require advanced analytics and machine learning
- Need open-source portability with enterprise features
- Want lakehouse architecture with Delta Lake
- Prioritize performance optimization (Photon engine)
- Value recent commitment to open-sourcing core components

---

## Methodology Note

This research was conducted using official documentation, technical blogs, and reputable sources current as of October 30, 2025. All findings are based on factual technical capabilities documented in official platform documentation and verified through multiple sources. Platform capabilities continue to evolve; verify current features for production decisions.

# DataOps Platform Capabilities: Technical Analysis for Scoring

Databricks emerges as the enterprise leader with comprehensive RBAC including unique ABAC capabilities and Unity Catalog governance, while Microsoft Fabric excels in real-time collaboration and environment management, and Keboola provides basic capabilities suitable only for small teams. This research reveals significant architectural differences that fundamentally impact each platform's suitability for enterprise DataOps, with security granularity, reproducibility infrastructure, and compliance maturity varying dramatically across the three platforms.

## RBAC (Role-Based Access Control)

### Platform Capabilities Comparison

**Databricks delivers the most sophisticated access control** with a complete five-level hierarchy from account to column level. The platform uniquely offers **Attribute-Based Access Control (ABAC)** through governed tags and reusable policies, representing an evolution beyond traditional RBAC. Unity Catalog provides row filters using SQL UDFs that evaluate at query time, and column masks that can conditionally redact data based on user context. Security policies are centrally managed and automatically applied to tagged objects across all catalogs and schemas, eliminating the need for table-by-table configuration. The platform supports native SCIM 2.0 provisioning, full SAML/OIDC integration, and treats service principals as first-class citizens with OAuth M2M authentication. Custom roles are created through flexible privilege combinations (SELECT, MODIFY, CREATE, USAGE, EXECUTE, READ FILES, WRITE FILES), and **privileges cascade through the catalog hierarchy** with USAGE propagation required at each level. Databricks scored the industry's most comprehensive security certifications and handles regulated industries with dedicated access modes (DBR 15.4 LTS+ required for RLS/CLS).

**Microsoft Fabric offers strong capabilities with notable architectural constraints**. The platform provides workspace-level RBAC with four predefined roles (Admin, Member, Contributor, Viewer) plus OneLake Security for granular data access. Row-level security uses SQL predicates with inline table-valued functions, while column-level security employs GRANT statements and dynamic data masking in four types (default, email, random, custom string). **The critical limitation**: workspace Admin/Member/Contributor roles override all OneLake RBAC Read permissions, creating an architectural challenge for zero-trust security models. OneLake Security remains in private preview requiring access requests at aka.ms/onelakesecuritypreview. The platform excels at Microsoft Entra ID integration with automatic JIT provisioning (default for accounts created after August 1, 2025) and supports full MFA through Entra authentication methods. Custom roles are supported for OneLake data (128 character max, alphanumeric) but not for workspace-level permissions. Role limits include 250 roles per lakehouse, 500 members per role, and 500 permissions per role, with propagation latency of 5 minutes for role changes and up to 2 hours including group membership and engine cache updates.

**Keboola provides only coarse-grained security** insufficient for enterprise requirements. Access control operates at organization → project → bucket level, with **no table, row, or column-level security**. The platform offers exactly seven predefined roles (Share, Admin, Guest, ReadOnly, Developer, Reviewer, Production Manager) with zero custom role capability. Buckets represent sets of tables as the smallest granular unit, making it impossible to control access to individual tables within a bucket. Identity integration is limited to SAML on Enterprise tier and Google OAuth, with **no SCIM or JIT provisioning** requiring manual user management. The platform supports MFA via TOTP and FIDO U2F hardware keys, with organization admins able to enforce MFA policies. Storage API tokens enable bucket-specific programmatic access, but the lack of fine-grained controls makes Keboola unsuitable for sensitive data requiring column-level protection or GDPR Article 32 compliance.

### Technical Implementation Details

Databricks implements row filters as **boolean-returning SQL UDFs** that leverage built-in functions like current_user() and is_account_group_member() for dynamic filtering. Column masks return the same data type as the masked column, supporting patterns like nullification, hashing, partial redaction (e.g., XXX-XX-1234), and conditional masking based on other column values. The ABAC system uses governed tags (key-value pairs on tables/columns) combined with centralized policy definitions that auto-apply to matching tagged objects. Runtime requirements mandate DBR 12.2 LTS minimum for row filters and column masks, with dedicated access mode in DBR 15.4 LTS+ required for full RLS/CLS functionality. Policies cannot be overridden by higher-level admins, and Delta Sharing does not support tables with RLS/CLS. Performance considerations favor simple SQL predicates over Python UDFs, which incur significant performance penalties.

Microsoft Fabric's OneLake Security implements **recursive inheritance** from workspace to item to folder/table levels, with the most permissive permission winning in conflict scenarios. The system creates virtual membership through dynamic role assignment based on item permissions (Read, Write, Reshare, Execute, ReadAll), and automatically generates DefaultReader/DefaultReadWriter roles. SQL-based security follows the principle that DENY takes precedence over GRANT, while shortcuts to external sources require delegated authentication plus OneLake security. Power BI reports with RLS/CLS must fall back to Direct Query mode rather than Direct Lake, impacting performance. Distribution lists cannot have members resolved by the SQL endpoint for OneLake roles. **Users with ReadAll permission can bypass security** by accessing data directly via Spark or OneLake APIs, creating potential audit blind spots.

Keboola's security model uses **token-based authorization** for programmatic access, with Storage API tokens providing bucket-specific access rights. The platform enforces CRYPT_BLOWFISH password hashing with 8+ character requirements and CAPTCHA after 10 failed login attempts within 5 minutes. Sessions timeout after 48 hours. Organization and project users operate as independent sets with no inheritance, requiring "Auto Join" features for maintainer/support access across projects. The flat permission model without cascading makes scaling difficult beyond approximately 50 users where manual provisioning becomes unmanageable.

### Comparative Scoring Analysis

**Databricks: 5/5** - Enterprise-grade excellence across all dimensions. The platform provides maximum flexibility with any custom privilege combination, most comprehensive fine-grained security including ABAC for scalable policy management, full native SCIM/SAML/OIDC/JIT support, Unity Catalog unified governance across clouds, comprehensive audit and automatic lineage, and no architectural security constraints. Suitable for Fortune 500, regulated industries (healthcare HIPAA, finance SOX, government), and complex data classification requirements.

**Microsoft Fabric: 4/5** - Strong capabilities with gaps. Comprehensive security features lose 0.5 points for preview status, 0.3 points for workspace override architectural limitation, and 0.2 points for limited custom workspace roles. Excels at Microsoft ecosystem integration with native Entra ID, strong SQL-based security features, and good hierarchy with inheritance. Best for Microsoft-centric organizations with Azure/M365 investment, medium enterprises (100-500 users), and standard RLS/CLS requirements without ABAC needs.

**Keboola: 2.5/5** - Inadequate for enterprise use. Fundamental limitations include bucket-level granularity only (-2.0 points for no table/row/column security), seven predefined roles with zero customization (-0.5 inflexibility), no SCIM/JIT support (-0.5 no automation), and manual provisioning that doesn't scale (-0.5). Only suitable for small teams under 50 users with simple, non-sensitive data and minimal compliance requirements. **Not recommended** for regulated industries, sensitive PII/PHI data, GDPR/HIPAA/SOX compliance requirements, or enterprise organizations.

## Reproducibility (Reproducibilita)

### Configuration Versioning Capabilities

**Databricks demonstrates the most mature version control integration** with comprehensive Git provider support including GitHub, GitLab, BitBucket, Azure DevOps, and AWS CodeCommit, plus on-premises versions (GitHub Enterprise Server, BitBucket Server/Data Center, GitLab Self-Managed, Azure DevOps Server). The platform's Git folders feature provides visual Git client and API directly integrated into the workspace, with notebooks automatically converted to source code format (.py, .scala, .sql, .r) in Git while preserving metadata like attached lakehouse and environment settings. Full branch management operates from the Databricks UI, supporting create, switch, merge, and rebase operations with visual diff comparison on commit and merge conflict resolution. Jobs can reference Git repositories directly with specific branches, tags, or commit hashes, eliminating the need for workspace copies and enabling true GitOps workflows. Legacy notebook Git integration was removed January 31, 2024, consolidating on the Git folders approach.

**Microsoft Fabric achieved General Availability for Git integration in 2024**, with Azure DevOps support (September 2024) and GitHub integration (July 2024). The workspace-level Git integration preserves folder structures up to 10 levels deep and provides item-level tracking for notebooks, reports, semantic models, pipelines, dataflows, lakehouses (metadata), warehouses (metadata), environments, and ML experiments/models (preview). Real-time sync status indicators appear in the workspace, with commit and update panels tracking changes. Branch management operates directly from the Fabric UI with checkout-to-new-branch feature preserving workspace state, pull request workflow support, merge conflict detection/resolution, and branch protection policies. Items are represented as directory structures in Git with JSON-based definitions, YAML for pipelines/environments, supporting declarative specifications. Full Git commit history enables rollback to previous commits via Update operations, with uncommitted changes tracked in the source control panel.

**Keboola takes a CLI-driven approach** with the Keboola CLI representing projects as directory structures with JSON files, enabling complete project definition in code. The native GUI-based virtual branching system creates shadow copies of entire projects for development/testing without production impact, while full Git integration supports GitHub, GitLab, and Azure DevOps via CLI functionality. The `kbc init --allow-target-env` mode enables GitOps management framework with automatic GitHub Actions workflow generation (pull, push, validate workflows), and Git operations through `kbc pull` and `kbc push` commands. Branch management supports mapping Git branches to Keboola GUI dev branches, with rename conflict handling during pull operations. All configurations (extractors, transformations, orchestrations) become definable in code with Variables Vault managing environment-specific parameters. The template repository system supports versioned templates using semantic versioning, enabling reusable project blueprints.

### Environment Management and Consistency

**Microsoft Fabric provides the most sophisticated environment promotion** through Deployment Pipelines supporting 2-10 stages (default: Dev/Test/Prod). The system enables selective or full deployment with deployment rules for parameterization, automatic dependency detection via "Select related" button, and autobinding of connected items across stages. Workspace-based environment separation assigns capacity per workspace with network security options (workspace-level security in preview). The "Branch out" feature creates new workspaces from branches, enabling complete environment isolation with separate capacities, VNet data gateway support, private link connectivity, and conditional access policies. Environment items track libraries and Spark dependencies with published state versus staging state, Git sync for environment definitions in Environment.yml format, and Spark compute configuration in YAML. Template-based workspace creation operates via Terraform for standardized provisioning.

**Databricks employs workspace-based separation** where different workspaces represent environments, with Unity Catalog metastore spanning workspaces for unified governance while maintaining isolated compute per workspace. Git-based promotion workflows move code branch-to-branch, while Terraform manages infrastructure with separate state files per environment. Environment-specific configurations use widget parameters for notebooks and job parameterization. Network isolation operates at the VPC/VNet level per workspace with private connectivity options and Unity Catalog catalog-level isolation. Git-based code distribution enables workspace cloning with Terraform-based provisioning and template-based setup via Terraform modules.

**Keboola offers virtual branching plus multi-project architecture**. Virtual branching creates lightweight branches for small/medium projects with complete data isolation through shadow copies, while multi-project architecture uses separate projects for complete environment isolation suitable for enterprise setups. The Project DevOps Manager (Private Beta) provides GitOps-based multi-environment management. CLI-based synchronization between environments leverages override target environment via KBC_PROJECT_ID and KBC_BRANCH_ID environment variables, Git-based promotion workflows with branch protection rules, and branch-merge-to-production patterns for releases. Complete data isolation in virtual branches contrasts with multi-project isolation using separate data warehouses. Template-based project creation, CLI-based project distribution (template to multiple projects), and full project export/import via CLI enable standardization.

### Dependency Management Sophistication

**Databricks provides the most flexible dependency management** across multiple scopes: cluster libraries installed at cluster level, notebook-scoped libraries via %pip and %conda magic commands, job libraries specified per task, and environment libraries through init scripts. The platform supports requirements.txt, conda environment.yml, Maven coordinates for JVM libraries, and custom package repositories from PyPI, Maven, and CRAN. Custom Docker containers enable "bring your own container" (BYOC) with Databricks runtime versions (DBR) providing reproducible base environments. DBR version pinning for clusters and jobs ensures consistent Spark versions, while library versions can be pinned in cluster definitions. Init script specification enables environment setup, and Unity Catalog registered models track environment metadata for ML reproducibility.

**Microsoft Fabric's Environment item** centralizes library and Spark dependency tracking with public libraries specified in YAML from PyPI or Conda, and custom libraries attached as .whl or .jar files. Requirements.yml format manages Python packages with library version specification (exact, range, or latest) and automatic compatibility resolution. Published environment states versus staging states provide clear separation, with Git sync for environment definitions and Environment.yml file format capturing complete specifications. Spark compute configuration in YAML and custom pool definitions (not fully supported in deployment pipelines yet) enable infrastructure definition. Default lakehouse parameterization in deployment rules ensures environment portability.

**Keboola leverages Docker-based components** with Python package management for Streamlit Data Apps through requirements.txt support and lock file support for Python 3.10 compatibility. Custom Docker images integrate via GitHub/GitLab with component deployment using semantic versioning (x.y.z tags) for reproducible runtime through Docker image tags. Version pinning in requirements.txt for Python packages, Docker image tags for reproducible deployments, template versioning with major.minor.patch format, and component version management in the Developer Portal enable dependency control, though the approach is more component-dependent than platform-integrated.

### Infrastructure-as-Code Maturity

**Databricks maintains the most mature Terraform provider** (databricks/databricks v1.26.0+ as of 2024) with comprehensive coverage across workspaces, clusters, jobs, notebooks, Unity Catalog, MLflow, SQL, storage, SCIM, secrets, and Git repos. Multi-cloud support spans AWS, Azure, and GCP. The **Resource Exporter tool** generates Terraform code from existing resources for infrastructure documentation and migration. Provider capabilities include workspace creation/management, cluster and instance pool definitions, multi-task workflow jobs, Unity Catalog configuration (catalogs, schemas, tables, grants), SCIM user/group management, MLflow experiments and registered models, SQL warehouse configuration, notebook deployment from Git, secrets management, and Git folder (repo) configuration. The Go-based Databricks SDK underlies the Terraform provider, with comprehensive REST APIs for all objects (API 2.0 for workspace/clusters/jobs, Unity Catalog API, SQL API, Repos API). Terraform state per environment with module-based reusability, variable files per environment (.tfvars), remote state storage (Azure Storage, S3, GCS), and CI/CD pipeline integration (GitHub Actions, GitLab CI, Azure DevOps) create mature deployment patterns.

**Microsoft Fabric achieved official Terraform provider GA in October 2024** with microsoft/terraform-provider-fabric covering workspaces, warehouses, lakehouses, notebooks, pipelines, semantic models, SQL databases, Eventhouse, and KQL databases. Authentication uses service principal or user credentials (transitioning to full SP support), with preview resources actively expanding coverage. ARM templates handle Azure Resource Manager templates for Fabric capacity provisioning (Microsoft.Fabric/capacities resource type) with Azure infrastructure integration. Comprehensive REST APIs enable all Fabric item management, workspace operations, Git API for programmatic sync, and deployment pipelines API for automation. Git-based declarative definitions with YAML for pipelines/environments, JSON for notebooks/other items, and infrastructure definitions via Terraform HCL provide complete configuration-as-code capabilities.

**Keboola relies on community-developed Terraform providers** (plmwong/terraform-provider-keboola and paybyphone/terraform-provider-keboola) used in production by enterprise customers but with limited maturity and documentation compared to official providers. Comprehensive public API enables all operations with the UI as a thin layer on top, CLI using public API without privileged access, and RESTful API for all components and configurations. The primarily declarative approach defines project state in JSON files with CLI sync operations comparing desired versus current state and push operations deploying configuration changes. GitHub Actions workflows (auto-generated), GitLab CI/CD pipeline support, Travis CI integration for component deployment, and automated testing/deployment pipelines enable deployment automation, though requiring more manual configuration than Databricks or Fabric.

### Deterministic Execution and Lineage

**Databricks Unity Catalog provides the most comprehensive lineage** with automatic capture (GA December 2022) occurring in real-time without configuration. Column-level lineage tracks dependencies for all operations across all languages (Python, SQL, R, Scala) in both batch and streaming modes. Near real-time visualization in Catalog Explorer shows privilege-aware lineage where users see only accessible data relationships. Table and notebook/job/dashboard lineage links to queries that produced data, with multi-workspace aggregation across all workspaces sharing the metastore. Lineage system tables (system.access.table_lineage, column_lineage) enable programmatic access via REST API, while "bring your own lineage" supports external non-Databricks assets. MLflow experiment tracking provides complete model training reproducibility, and Delta Live Tables expectations enforce data quality. DBR version pinning ensures consistent Spark and library versions, Git commit hashes track job code versions, and Delta Lake time travel queries historical data versions with full change history. Delta Lake ACID properties provide atomic, consistent operations with merge operations supporting upsert patterns for idempotency, structured streaming checkpointing enables exactly-once semantics, though job idempotency depends on user implementation.

**Keboola delivers automatic data lineage** as a key differentiator, generating real-time lineage from source to destination with column-level dependency tracking and **OpenLineage standard compatibility**. Visual lineage graphs span entire pipelines with impact analysis for schema changes, metadata capturing all modifications, and schema evolution tracked automatically. Lineage integrates with external catalogs including Informatica, Collibra, DataHub, and Manta. Job-level metadata tracking with version-specific component execution, Docker image tagging for reproducible runtimes, and configuration snapshots in Git enable execution reproducibility. Git-based configuration snapshots, virtual branch snapshots preserving data state, job execution history and metadata, and telemetry data for job runs provide checkpointing, though idempotency remains configuration-based and not automatic, with component-specific support varying by component.

**Microsoft Fabric's lineage view** in workspace shows item dependencies with table and column-level lineage for supported items, cross-workspace lineage visibility, and upstream/downstream dependency tracking. Dataflow lineage support and ML experiment/model lineage (preview) continue expanding. Real-time lineage updates provide visual lineage graphs with external data source connections and impact analysis for changes, while deployment pipeline maintains lineage across stages. Published environment states ensure consistent runtime with Spark runtime versioning, library version locking, and Git-based code version control. Git commit snapshots, deployment pipeline stage snapshots, warehouse/lakehouse time travel through underlying Delta Lake, and environment published versus staging states enable restoration, though idempotency is not automatically guaranteed and depends on pipeline design. Delta Lake ACID properties for data operations, incremental refresh for semantic models, and dataflow Gen2 refresh patterns provide some determinism.

### Scoring Recommendations

**Databricks: Overall 4.8/5** - Version Control (5/5) with mature, comprehensive, native Git integration; Environment Management (4/5) flexible and powerful but requires more setup than Fabric; Dependency Management (5/5) most comprehensive with container support and DBR versioning; IaC/Terraform (5/5) most mature provider with resource exporter; Recreate from Code (5/5) comprehensive Terraform + Git + APIs; Deterministic Execution/Lineage (5/5) Unity Catalog automatic, comprehensive, real-time column-level lineage.

**Microsoft Fabric: Overall 4.5/5** - Version Control (4/5) GA 2024, comprehensive and rapidly improving; Environment Management (5/5) best deployment pipelines with autobinding and rules; Dependency Management (4/5) environment items improving but less mature than Databricks; IaC/Terraform (4/5) GA 2024 with good coverage actively expanding; Recreate from Code (4/5) Terraform GA, Git improving; Deterministic Execution/Lineage (3.5/5) lineage view improving but less mature than Databricks, lacking automatic column-level capture.

**Keboola: Overall 3.5/5** - Version Control (3.5/5) CLI-based, powerful but requires more manual setup; Environment Management (4/5) virtual branching + multi-project flexible and effective; Dependency Management (3/5) Docker-based but component-dependent; IaC/Terraform (2/5) community-only, limited documentation and maturity; Recreate from Code (4/5) CLI + templates powerful but manual; Deterministic Execution/Lineage (4/5) automatic lineage with OpenLineage excellent, telemetry strong.

## Sharing & Collaboration (Sdílení/Kolaborace)

### Real-Time Collaboration Features

**Microsoft Fabric and Databricks both deliver true real-time co-editing**, while Keboola lacks this capability entirely. Fabric notebooks support simultaneous editing with multiple users able to modify the same notebook concurrently, featuring live presence indicators showing collaborator profiles, cursor indicators displaying where others are editing, selection highlights showing what others have selected, editing traces revealing changes in real-time, and run outputs visible to all collaborators. Cell-level comments enable contextual discussions with @mention functionality triggering email notifications, tagging users without access prompting automatic permission requests, and comment threads supporting Edit, Resolve, and Delete options. Auto-save operates by default (can be disabled) with version history creating automatic checkpoints every 5 minutes and manual checkpoints for milestones. Git-based conflict resolution provides merge conflict flagging during operations with side-by-side diff view for manual resolution before merge completion.

**Databricks provides comparable real-time collaboration** with simultaneous notebook editing, "co-presence" indicators showing active users, editing activity visible to all collaborators, and shared run outputs. Inline comments attach to specific code sections with @mention support for direct notifications, comment threads on code blocks, email notifications for comment activity, comments sidebar for navigation, and edit/delete/resolve options. Automatic versioning of all changes prevents data loss with revision history enabling restore capabilities, while Git-based conflict resolution and version control track changes. Databricks Assistant provides contextual help during collaboration.

**Keboola offers no real-time collaboration features**. Workspaces serve as individual development environments without Google Docs-style simultaneous editing, no co-authoring capabilities, no live cursors or presence indicators, no inline commenting in code, and no discussion threads within workspaces. Multiple users can work in separate workspaces on the same backend, but workspace-to-transformation conversion provides the only collaboration path by finalizing code for sharing. Communication happens outside the platform with no integrated discussion features.

### Data Sharing and Distribution

**Databricks leads with Delta Sharing**, the open-source protocol for secure data sharing that works cross-platform with any Delta Sharing-compatible client across AWS, Azure, GCP, and on-premises environments. The platform shares tables, views, notebooks, ML models, and volumes with read-only access for recipients, achieving 300%+ YoY growth in active shares during 2024. Full Apache Iceberg support (Public Preview 2025) enables sharing Iceberg tables via Delta Sharing to Snowflake, AWS Glue, and other platforms. **Databricks Marketplace** (General Availability) operates as an open marketplace for data/AI assets with 600+ million business records available from providers like Dun & Bradstreet, supporting datasets, notebooks, applications, and ML models without vendor lock-in. Delta Sharing connectors support Apache Spark, Pandas, Power BI, Tableau, and other tools with 16,000+ data recipients across platforms, 40% using open connectors for cross-platform access. **Databricks Clean Rooms** (GA 2024 on AWS, Azure, GCP) enables privacy-safe collaboration without sharing raw data across up to 10 organizations, supporting SQL, R, Scala, Java, Python with secure self-runs using notebook approval workflows and privacy-centric identity resolution. Unity Catalog provides centralized data governance with catalog explorer for discovery, cross-workspace model sharing, row-level and column-level security, and ABAC with storage credentials for secure cloud access.

**Microsoft Fabric launched External Data Sharing** (General Availability November 2024) enabling cross-tenant sharing of Lakehouse, Warehouse, KQL Database, and Mirrored databases. In-place sharing requires no data copying with email invitation systems, where recipients accept and create OneLake shortcuts maintaining read-only data for consumers. Microsoft Entra B2B guest accounts provide external user authentication with security group-based access control requiring Premium Per User or Fabric capacity. OneLake shortcuts enable data access with proprietary Fabric sharing mechanism and API support for external sharing workflows, though lacking Delta Sharing support. Governance features include admin controls for cross-geo exports, tenant settings controlling external sharing, sensitivity label policies via Microsoft Purview, and Data Loss Prevention (DLP) policies. Power BI provides **comprehensive embedding capabilities** with "Embed for your organization" for internal users and "Embed for your customers" for external applications. F64+ capacity allows free license users to view content while F32 and lower require Pro licenses. Service principal authentication enables "app owns data" scenarios with SharePoint embedding for organizational distribution and Teams integration for collaborative discussions. Direct sharing of reports and dashboards includes customizable permissions (read-only, build permissions, reshare rights) for "people in your organization" or specific users. "Publish to Web" creates public URLs though not recommended for sensitive data.

**Keboola's Data Catalog** serves as the central feature for sharing data across projects, sharing by buckets (collections of tables) with "Shared with everyone" or "Shared with specific projects" options. Shared buckets become instantly available to other projects in the organization with **live data** updating automatically as source data changes, using one-click subscription model for consumers. Datashare Owner assignment to buckets tracks responsibility with metadata editing for descriptions, custom colors, and ownership. List view provides filtering options (All, Linked, or Mine) for certified data products with data contracts as governance features. Read-only access for linked buckets by default prevents modifying shared bucket data in consuming projects, with sharing managed at project administrator level and token-based sharing for specific resources. External sharing is **limited**, requiring creation of new Keboola projects for contractors with data shared into external projects, since true cross-organizational sharing capabilities are constrained. Data Apps can be deployed publicly but traditional embedding is not a primary feature. The Component Marketplace offers 3rd party applications with components that can be private or shared organization-wide, and Data Catalog serves as an internal marketplace that is searchable and filterable with metadata.

### Export/Import Interoperability

**Databricks provides the most comprehensive export formats**: DBC Archive (proprietary binary format including metadata and outputs), IPython Notebook (.ipynb) as standard Jupyter format, HTML for web sharing, RMarkdown (.Rmd) for R notebooks, and Source File formats (.py, .scala, .sql, .r) as plain text code. ZIP archives enable bulk export with options to include/exclude cell outputs and export single notebook or folder structures. Import supports URL or local file for .ipynb, .py, .scala, .sql, .r, .Rmd, DBC, and ZIP formats, preserving folder structure. **Databricks CLI** provides export_dir/import_dir commands for bulk operations, Git integration for version-controlled migration, REST API for programmatic transfers, cross-workspace sharing via Unity Catalog, and model registry for ML model migration. Delta Sharing connectors extend to Apache Spark, Pandas, Power BI, Tableau, and custom integrations via JDBC/ODBC for SQL access with Unity Catalog metastore sharing across workspaces.

**Microsoft Fabric supports multiple formats**: Notebooks export as .ipynb (Jupyter), .py (Python), .sql, .scala, HTML, and .tex formats, with Git format commits to Azure DevOps/GitHub repositories. Power BI exports .pbix files and .pbip (project format), while Data Warehouse uses DacFx (Data-tier Application packages). Semantic models export with configurations. Import mechanisms handle .ipynb, .py, .sql, .scala files from URLs or local storage, Git sync from Azure DevOps/GitHub, PBIX file import, and DacFx import for warehouse schemas. Migration tools include Deployment Pipelines for Dev/Test/Prod promotion, Git integration for version control, DacFx for warehouse lifecycle management, export/import for cross-workspace migration, and "Branch Out" feature creating isolated development workspaces. REST APIs enable programmatic access with Azure Data Factory integration, Power Automate for workflow automation, Synapse Analytics compatibility, and cross-platform data access via OneLake shortcuts.

**Keboola emphasizes data movement**: CSV files as primary export format for tables, JSON for configuration exports, and **Data Takeout** exporting entire project contents to S3 with all tables in CSV format (gzipped), all configurations in JSON, configuration versions and transformation queries, and encrypted values remaining encrypted. Files organize into /in/, /out/, /sys/, /configurations/ folders. CSV Import component loads data, Storage import connector loads tables from other Keboola projects, HTTP connector fetches CSV files from URLs, and OneDrive Excel Sheets import is supported. Data Takeout provides project snapshots (export-only) but cannot automatically import full projects (requires Keboola Support), though Keboola Storage connector writes tables to different Keboola projects. **700+ native integrations** with sources and destinations enable API-based data exchange with Keboola CLI for command-line operations and Storage API for programmatic access.

### Collaboration Infrastructure

**All three platforms support team management** with varying sophistication. Databricks provides five permission levels (NO PERMISSIONS, CAN READ, CAN RUN, CAN EDIT, CAN MANAGE) where CAN READ allows viewing cells, commenting, and running via %run; CAN RUN adds attach/detach and run commands; CAN EDIT adds cell editing; and CAN MANAGE provides full control including permissions. Workspace admins have CAN MANAGE on all notebooks with folder-based permission inheritance and security groups via identity providers. Git integration supports Azure DevOps, GitHub, BitBucket, and GitLab for cloning repos, creating projects, branch management, and CI/CD pipeline integration. Email notifications support @mentions in comments and job execution notifications.

Microsoft Fabric offers four workspace roles (Admin, Member, Contributor, Viewer) where Admin has full control including manage permissions and delete workspace; Member can create/modify items and add members; Contributor can create/modify items but cannot manage access; and Viewer has read-only access. Security groups, Microsoft 365 groups, and distribution lists are supported with nested user groups and permission inheritance. SharePoint integration provides document collaboration with Microsoft 365 Group integration for unified access management. Git Integration (GA) supports Azure DevOps and GitHub with branch management, "Branch Out to New Workspace" for isolated development, private workspace + shared workspace patterns, and conflict resolution during merge. Contact lists enable workspace notifications with email notifications for changes and @mentions in notebook comments with email notifications.

Keboola's multi-project architecture supports separation by teams, departments, or business units with project-level access control and role-based permissions. Project administrators assign roles and permissions with each project operating as self-contained workspace having isolated storage and configurations. Workspaces (formerly "Sandboxes") serve as isolated development environments supporting Python/R with JupyterLab and SQL workspaces (Snowflake, BigQuery, Redshift). Workspace sharing enables read-only or full-access modes with no workspace locking mechanism, and multiple users can have multiple workspaces on the same backend. Auto-backup functionality in Python/R workspaces and auto-sleep features after inactivity reduce costs. Workspaces convert to transformations and vice versa, but with no real-time co-editing and no locking mechanism for concurrent access. Projects organize by use cases, teams, or departments with horizontal, vertical, or hybrid split designs, with workspace backend sizes adjustable for computational needs.

### Scoring Assessment

**Real-time Collaboration**: Keboola 1/5 (no real-time features), Microsoft Fabric 5/5 (full co-editing with presence, cell-level comments, @mentions, notifications), Databricks 5/5 (full co-editing with commenting, co-presence).

**Dashboard/Report Sharing**: Keboola 2/5 (limited, data-focused not visualization-focused), Microsoft Fabric 5/5 (Power BI embedding comprehensive with "embed for your organization/customers", direct sharing, workspace apps), Databricks 4/5 (SQL dashboards, API access, not as BI-focused as Fabric).

**Export/Import**: Keboola 4/5 (comprehensive CSV/JSON/Data Takeout but proprietary), Microsoft Fabric 5/5 (Git, multiple formats, APIs, DacFx, deployment pipelines), Databricks 5/5 (DBC, .ipynb, CLI, APIs, comprehensive).

**Cross-organization Sharing**: Keboola 2/5 (limited, requires separate projects, no open protocols), Microsoft Fabric 4/5 (external data sharing, tenant boundaries, proprietary but functional), Databricks 5/5 (Delta Sharing open protocol, Marketplace, Clean Rooms, cross-cloud/cross-platform, 16,000+ recipients).

**Commenting/Annotations**: Keboola 2/5 (descriptions only, no inline comments, no discussions), Microsoft Fabric 5/5 (cell-level, @mentions, notifications, Teams integration), Databricks 5/5 (code-level, @mentions, email integration, Assistant).

**Overall Collaboration Maturity**: Databricks and Microsoft Fabric tie at approximately 4.8/5 for different reasons (Databricks for open data sharing and marketplace, Fabric for real-time development and enterprise integration), while Keboola scores 2.5/5 (adequate for internal data governance but lacking modern collaboration features).

## Auditability (Auditovatelnost)

### Audit Logging Scope and Implementation

**Databricks captures the most comprehensive audit events** with over 100 distinct audit action types spanning workspace-level and account-level events. User actions logged include login attempts and authentication events, cluster creation/deletion/modification, notebook execution and access, SQL query execution via Databricks SQL, job creation and execution, ACL modifications, storage access (DBFS, Unity Catalog), model registry operations, Delta Sharing activities, and Git repository interactions. System events cover cluster lifecycle (start, stop, resize, terminate), auto-scaling activities, job scheduler events, Unity Catalog metadata operations, data lineage capture, system table updates, billing/usage events, and storage access from compute plane. **Enhanced Security Monitoring logs** (add-on feature) include file integrity monitoring, antivirus scanning, and process monitoring. JSON format provides structured logging with consistent schema across event types, delivered to customer-owned cloud storage (S3/ADLS/GCS) with system tables (system.access.audit) in Delta Lake format enabling SQL queries. Query audit logs use Unity Catalog system tables tracking all data access with column-level lineage including query attribution, user email, timestamp, and full query text (when verbose mode enabled) through commandSubmit, getTable, createTable, deleteTable actions.

**Microsoft Fabric provides comprehensive coverage** across the platform with user logins via workspace authentication, data access (Lakehouse, Data Warehouse, Power BI), configuration changes (workspace, capacity, domain settings), notebook executions, SQL queries via Data Warehouse, pipeline runs (Data Factory activities), Spark activities, sensitivity label changes, and permission modifications. System events include capacity metrics and utilization, workspace creation/deletion/modification, item creation/deletion (Lakehouses, Warehouses, Notebooks), scheduled job executions, data refresh operations, pipeline orchestration events, and audit log delivery status. Event-level logging captures all Fabric activities with service-specific logs (databrickssql, cluster, notebooks) including request and response details, user identity, IP address, and timestamp for each event. Structured JSON format provides consistent fields across events, while SQL Audit Logs store in .XEL files (Extended Events) queryable via sys.fn_get_audit_file_v2 function. **SQL Data Warehouse comprehensive query auditing** (preview 2024) captures T-SQL statements, user, timestamp, event type, authentication attempts, access control changes, DML and DDL operations, and commandSubmit, getTable, createTable, deleteTable events.

**Keboola tracks operational essentials** including user login/logout events, data access at table and bucket level, configuration changes to components and flows, token creation and usage, job executions and transformations, schema evolution tracking, and data pipeline performance metrics. System events cover job status (success/failure/running), data flow between components, ETL/ELT pipeline execution, credit unit consumption per job, automated workflow triggers, and component configuration changes. Event-level metadata captures all operations with user activity tracking at individual action level, job-level tracking with detailed execution logs, comprehensive operational metadata including runtime/costs/errors, and bucket-level (dataset group) access control and tracking. Metadata is captured in structured format accessible via project metadata tables, integrating with **OpenLineage standard** for metadata interchange, with Jobs section providing detailed logs with timestamps. Full audit trail tracks who accessed what data and when through token-based authorization system logging all data access, granular tracking down to bucket (dataset group) level, and query execution logs available through Storage Jobs interface.

### Retention and Access Infrastructure

**Microsoft Fabric offers the longest configurable retention** with SQL Audit Logs supporting **up to 9 years** configurable retention, default Power BI activity logs with 7-day default search window, Fabric retaining copy of audit logs for up to 1 year for security/fraud analysis, configurable retention in OneLake for SQL audit logs, and Purview Audit log retention based on Microsoft 365 licensing. Access methods include Microsoft Purview compliance portal as primary access point, web UI via Fabric Admin Portal → Audit Logs tab, SQL queries using sys.fn_get_audit_file_v2 T-SQL function, REST API via Fabric API for audit log configuration, PowerShell Get-PowerBIActivityEvent cmdlet, and export to CSV from Purview portal. **Native Azure Sentinel** integration for SIEM with Splunk support via Purview integration, Event Hubs integration for real-time streaming, Azure Monitor Log Analytics integration, and third-party SIEM tools via Azure diagnostic settings provide comprehensive monitoring. Most events appear within 30-60 minutes with real-time event-driven notifications via webhooks and batch scheduled exports to OneLake/Azure Storage. Storage costs in OneLake can be significant with broad action groups (recommendation: enable only required events), Purview Audit included with Microsoft 365 E5/E3 or as add-on, and separate Azure Monitor integration costs.

**Databricks retains audit logs** with platform copy up to 1 year for security/fraud analysis, customer-owned storage retention indefinite (customer controlled), Unity Catalog audit logs 90 days default (can export for longer retention), system tables providing queryable access to retained logs, and recommendation to export to long-term storage (S3/ADLS) for compliance requirements. System tables enable SQL queries via system.access.audit, web UI provides limited access to recent events, REST API configures audit log delivery, customer cloud storage allows direct file access to JSON logs, and log delivery automates to customer S3/ADLS/GCS buckets. Native integration with major SIEMs (Splunk, Azure Sentinel, etc.) leverages JSON format for easy parsing, Delta Lake format for advanced analytics, Databricks used internally as SIEM/XDR platform, Structured Streaming for real-time ingestion, and compatibility with MITRE ATT&CK framework. Batch delivery provides periodic file drops to cloud storage with near real-time access through system tables, Enhanced Security Monitoring logs streamed to audit logs, typical SLA delivering logs within hours, and Delta Live Tables processing audit logs in real-time pipelines. Audit log storage in customer cloud accounts incurs standard cloud storage costs, system tables storage included in platform pricing, Enhanced Security and Compliance add-on priced separately, with no separate charge for basic audit logging.

**Keboola provides operational retention** with Snowflake backend offering 7 days of historical data via time travel, Amazon Redshift supporting multiple snapshots per day for recovery, operational metadata retained within project indefinitely for analysis, and jobs logs accessible through project interface. Web UI provides access through Jobs section and Storage interface, API access retrieves all project metadata, direct query access to operational metadata tables, and export capabilities enable downstream analysis. OpenLineage compatibility enables metadata export, API-first architecture allows integration with external tools, metadata accessible for ingestion by SIEM platforms, and custom integration possible via REST API. Real-time access to job execution logs with metadata generated automatically as pipelines run provides immediate visibility into pipeline status and failures. Audit trails are included in platform pricing with no separate charges for operational metadata storage, and cost attribution tracking included (tracks credit usage per job/user/team).

### Compliance Certifications and Support

**Databricks holds the most comprehensive certification portfolio** as of 2024: SOC 2 Type II (updated 3x per year in June, August, December), SOC 3 (publicly available report), ISO 27001:2013, HIPAA (Enhanced Security and Compliance add-on), HITRUST CSF (Azure Databricks), FedRAMP High (AWS GovCloud), FedRAMP Moderate, PCI-DSS (Enhanced Security and Compliance add-on), IRAP (Australia), C5 (Germany), UK Cyber Essentials Plus, K-FSI (Korea Financial Security), and Canada Protected B (CCCS Medium). Industry-specific compliance includes healthcare (HIPAA and HITRUST CSF), government (FedRAMP High/Moderate, IRAP), and financial (PCI-DSS, K-FSI) with compliance security profiles available for each standard. Enhanced Security and Compliance add-on is required for most stringent certifications. Trust Center at databricks.com/trust provides due diligence packages with ISO certifications, penetration test confirmations, Enterprise Security Guide for customers, SOC 2 Type II reports via account team, Security Addendum in customer agreement, and regular independent third-party audits.

**Microsoft Fabric certifications** for 2024 include SOC 1 Type II, SOC 2 Type II, SOC 3, ISO/IEC 27001, ISO/IEC 27017 (cloud security), ISO/IEC 27018 (cloud privacy), ISO/IEC 27701 (privacy management), HIPAA Business Associate Agreement coverage, and FedRAMP for government customers. Industry-specific compliance covers healthcare (HIPAA BAA), government (FedRAMP authorization), and financial services with comprehensive audit trails. Service Trust Portal (servicetrust.microsoft.com) provides audit reports and compliance documentation via Microsoft Trust Center as primary resource with downloadable compliance documents (SOC reports, certifications), Online Services Terms and Data Protection Addendum, and regular third-party audits. Microsoft Purview Information Protection enables data classification with sensitivity labels for data protection, DLP policies, right to access supported via export capabilities, data deletion controls, and data residency via regional capacities.

**Keboola maintains essential certifications**: SOC 2 Compliant, ISO 27001 Compliant, HIPAA Compliant, PCI Compliant, FedRAMP Compliant, CSA Star Level 1 Compliant, and GDPR Compliant since May 25, 2018. Industry-specific compliance addresses healthcare (HIPAA), financial services (PCI), government (FedRAMP), and general enterprise security standards. Data Processing Addendum (DPA) is publicly available with security documentation on website, compliance certifications listed and accessible, and regular security audits by independent third parties. GDPR features include Data Processing Addendum publicly available, right to access where users can download all content, right to deletion via project deletion with complete data removal, data processor and data controller roles defined, Privacy Officer appointed, and international data transfer controls in place.

### Data Governance and Tracking

**Databricks Unity Catalog provides built-in automatic lineage capture** with column-level lineage (Runtime 13.3 LTS+) across all languages (SQL, Python, Scala, R) in real-time within Catalog Explorer. Lineage system tables (system.access.table_lineage, column_lineage) enable programmatic queries with cross-workspace lineage aggregation, external lineage metadata support (public preview), and one-year rolling window for lineage data. User identity tracking captures user_identity.email in all audit events, service principal identification, SSO integration (Azure AD, Okta, Ping Identity), Personal Access Token usage tracked, and impersonation tracking (impersonatedBy field). Action attribution includes action_name for specific operations, service_name identifying Databricks service, request_params with detailed operation parameters, response with operation results and status codes, and query text captured for SQL operations. Event_time provides millisecond precision timestamps with event_date partitioning for efficient queries, duration tracking for long-running operations, and start/end times for jobs/queries. Regional deployment options (AWS, Azure, GCP) keep data within specified cloud region with Unity Catalog metastore per region, cross-region controls, and Private Link support for network isolation. Customer-managed keys (CMK) supported with default encryption via cloud provider (AWS KMS, Azure Key Vault, GCP KMS), TLS 1.2+ for all connections, inter-node encryption (Enhanced Security add-on), and FIPS 140-2 Level 1 validated modules (compliance profiles).

**Microsoft Fabric Purview integration** delivers end-to-end lineage with item-level lineage for Fabric artifacts, Power BI dataset lineage, Lakehouse table lineage (preview - sub-item level coming), cross-workspace lineage visibility, and visual lineage graphs in Purview. User_identity.email is captured in all audit logs with Azure Active Directory (Entra ID) integration, service principal identification for automated workloads, user subject name and profile information, and impersonation tracking when applicable. Action_name field identifies specific operations, service_name identifies Fabric component, request_params contains operation details, response object includes status and results, and operation list with 100+ distinct audit actions. Event_time provides precise UTC timestamps with event_date partitioning for efficient queries, millisecond precision timestamps, and start/end time for long-running operations. Regional capacity deployment controls with data processing location specified in Online Services Terms, multi-geo capabilities for global organizations, and workspace assignment to specific regions enable residency. Default encryption in OneLake with customer-managed keys (CMK) support in roadmap, TLS 1.2+ for all communications, and SQL Audit Logs encrypted at rest in OneLake provide security.

**Keboola's automatic data lineage** generates real-time lineage from source to destination with column-level dependency tracking, OpenLineage standard compatibility, visual lineage graphs across entire pipeline, impact analysis for schema changes, metadata capturing all modifications, and schema evolution tracked automatically. User email and identity captured in all events with token-based authorization system for all actions, SAML integration with Active Directory supported, Google Authentication supported, and MFA available (phone app or hardware keys) with organization admins able to enforce MFA. Every operation logged with user identity, job execution tracked to specific users, configuration changes attributed to users, and component creation and modification tracked. Event-level timestamps for all operations with job execution start/end times recorded and detailed timing for performance analysis. Multiple deployment regions (AWS, Azure, GCP) with single-tenant deployment option for maximum control, multi-tenant with BYO (Bring Your Own) database, and data stays in specified cloud region. Latest AWS/Azure encryption policies at rest with keys managed by AWS Key Management Service, HTTPS/TLS for all transport channels in transit, and SSL encryption for REST API connections.

### Comparative Scoring

**Audit Logging Capabilities**: Databricks 5/5 (100+ action types, comprehensive, granular), Microsoft Fabric 5/5 (comprehensive coverage, SQL query auditing), Keboola 4/5 (good operational coverage, OpenLineage).

**Log Retention/Accessibility**: Microsoft Fabric 5/5 (up to 9 years, multiple access methods, Purview integration), Databricks 4.5/5 (1 year platform, unlimited customer storage, system tables), Keboola 3/5 (7 days Snowflake, indefinite metadata, limited compared to others).

**Compliance Certifications**: Databricks 5/5 (12+ frameworks including FedRAMP High, most comprehensive), Microsoft Fabric 4.5/5 (comprehensive Microsoft certifications, strong but fewer than Databricks), Keboola 4/5 (essential certifications covered, adequate for most uses).

**Who/What/When Tracking**: All three platforms 5/5 (comprehensive identity tracking, timestamps, action attribution, IP addresses).

**Change Tracking/Lineage**: Databricks 5/5 (Unity Catalog automatic column-level lineage, comprehensive), Keboola 4.5/5 (automatic lineage, OpenLineage standard, excellent), Microsoft Fabric 4/5 (Purview integration, improving, item-level).

**Regulatory Compliance**: Databricks 5/5 (CMK, most flexible, Enhanced Security add-on, compliance profiles), Microsoft Fabric 4.5/5 (strong Microsoft compliance, regional controls), Keboola 4/5 (adequate data residency, encryption, compliance features).

**Overall Auditability**: Databricks 4.9/5 (most comprehensive audit capabilities, certifications, and governance), Microsoft Fabric 4.7/5 (longest retention, excellent Microsoft ecosystem integration), Keboola 4/5 (adequate for most use cases, strong lineage, limited retention).

## Cross-Platform Synthesis

### Enterprise Suitability Matrix

For **large enterprises requiring maximum security and compliance** (500+ users, regulated industries including healthcare HIPAA, finance SOX, government), Databricks emerges as the clear leader. The platform's unique ABAC capabilities enable scalable, centralized policy management where security policies follow data based on sensitivity tags rather than requiring hundreds of table-specific rules. Unity Catalog provides unified governance across AWS, Azure, and GCP with automatic column-level lineage, comprehensive audit logging with 100+ action types, and the industry's most extensive certification portfolio including FedRAMP High. Service principals operate as first-class citizens with OAuth M2M authentication, native SCIM 2.0 provisioning eliminates manual user management at scale, and mature Terraform provider (v1.26+) with Resource Exporter enables complete infrastructure-as-code. Delta Sharing as an open protocol combined with Databricks Marketplace and Clean Rooms positions the platform for external data monetization and privacy-safe collaboration across organizational boundaries.

**Microsoft-centric organizations** (100-500 users, Azure/M365 investment) find Microsoft Fabric optimally integrated with their existing infrastructure. The platform achieved General Availability for critical features in 2024 including Git integration and External Data Sharing, while Deployment Pipelines provide superior environment management with 2-10 configurable stages, automatic dependency detection, and autobinding of connected items. Real-time notebook co-editing with presence indicators, cell-level commenting, and @mention notifications delivers the strongest developer collaboration experience. SQL Audit Logs support up to 9 years retention (longest of the three platforms) with native Azure Sentinel integration and Microsoft Purview providing comprehensive compliance reporting. The workspace override limitation where Admin/Member/Contributor roles bypass OneLake RBAC Read permissions requires architectural consideration, necessitating Viewer role assignment for data consumers to enforce fine-grained security. OneLake Security remains in private preview requiring access requests, limiting production readiness for organizations requiring GA feature status.

**Small to medium teams** (under 50 users, simple data workflows, minimal compliance requirements) may find Keboola's straightforward approach sufficient. Automatic data lineage with OpenLineage standard compatibility, live data propagation across projects through Data Catalog, and virtual branching plus multi-project architecture provide adequate capabilities for basic DataOps. The fundamental limitation of bucket-level granularity (no table, row, or column-level security) combined with seven predefined roles without customization capability makes Keboola **unsuitable for enterprises, regulated industries, or any sensitive data** requiring GDPR Article 32, HIPAA Security Rule, or SOX compliance. Community-developed Terraform provider lacks maturity compared to official providers from Databricks and Microsoft, and absence of real-time collaboration features (no co-editing, no inline comments, no presence indicators) positions Keboola behind modern expectations for platform collaboration.

### Critical Differentiators for Thesis Analysis

**ABAC represents the evolution of data governance** beyond traditional RBAC. Databricks' governed tags and reusable policies enable defining security once with automatic application to all matching tagged objects across catalogs and schemas, eliminating table-by-table configuration overhead. For example, tagging all tables containing SSN data with "PII=high" allows a single centralized policy to mask for all non-admin users, with table owners unable to bypass policies controlled by data governance teams. Neither Fabric nor Keboola offer ABAC capabilities, representing a generation gap in access control sophistication that matters significantly for large-scale data platforms with hundreds or thousands of tables requiring classification-based security.

**Environment reproducibility through IaC maturity** varies dramatically. Databricks' Terraform provider at v1.26+ with Resource Exporter tool generates infrastructure code from existing resources, comprehensive module support, and multi-cloud deployment patterns represents production-grade infrastructure-as-code. Microsoft Fabric achieved official provider GA only in October 2024 with actively expanding coverage but less maturity. Keboola relies entirely on community-developed providers without official support, creating risk for enterprise infrastructure automation. This technical debt compounds over time as platforms scale, with Databricks enabling complete workspace recreation from code while Keboola requires manual intervention for project imports.

**Data lineage granularity** impacts both compliance and operational efficiency. Databricks Unity Catalog provides automatic **column-level lineage** in real-time across all languages with cross-workspace aggregation and one-year rolling history, enabling precise impact analysis when schema changes occur and supporting GDPR/CCPA data mapping requirements at the finest granularity. Keboola delivers automatic table and column-level lineage with excellent OpenLineage standard compatibility for external catalog integration. Microsoft Fabric provides item-level lineage via Purview with column-level capabilities improving but less mature than Databricks. For regulated industries requiring comprehensive data lineage documentation, the automatic capture without configuration overhead in Databricks and Keboola contrasts with Fabric's need for Purview integration and configuration.

**Real-time collaboration maturity** separates modern platforms from legacy approaches. Both Databricks and Microsoft Fabric deliver Google Docs-style simultaneous notebook editing with presence indicators, live cursors, and inline commenting with @mentions triggering email notifications. This enables genuinely collaborative development where data engineers, analysts, and data scientists work together synchronously. Keboola's complete absence of real-time collaboration features—no co-editing, no presence indicators, no inline comments, no discussion threads—relegates the platform to individual development followed by asynchronous sharing, fundamentally limiting team velocity and coordination effectiveness in modern distributed work environments.

**Cross-organizational data sharing** architecture reveals strategic platform positioning. Databricks' Delta Sharing as an open-source protocol with 16,000+ data recipients and 40% using open connectors enables vendor-neutral data monetization and ecosystem participation. Databricks Marketplace with 600+ million business records and Clean Rooms for privacy-safe multi-party collaboration position the platform for external data business models. Microsoft Fabric's External Data Sharing (GA November 2024) provides functional cross-tenant sharing but with proprietary mechanisms creating potential vendor lock-in. Keboola requires creating separate projects for external parties with limited true cross-organizational capabilities, suitable only for occasional contractor access rather than systematic data product distribution.

### Scoring Justification Methodology

The 1-5 scoring scale applied consistently across metrics: **5 = excellent, comprehensive, enterprise-grade** with no significant gaps and industry-leading capabilities; **4 = strong with minor limitations** suitable for most enterprise use cases with documented workarounds for gaps; **3 = adequate with some gaps** functional for standard use cases but requiring careful evaluation of limitations; **2 = limited with significant gaps** suitable only for simple use cases or small scale; **1 = poor or minimal capabilities** inadequate for production enterprise use.

**Databricks consistently scores 4.8-5/5** across metrics due to comprehensiveness without architectural constraints. RBAC scores 5/5 for ABAC uniqueness, complete fine-grained security, native SCIM/JIT, and Unity Catalog governance. Reproducibility scores 4.8/5 with minor deduction only for environment management requiring more setup than Fabric's Deployment Pipelines. Collaboration scores 4.8/5 for real-time co-editing and Delta Sharing/Marketplace leadership despite Power BI embedding being less mature than Fabric. Auditability scores 4.9/5 for most comprehensive audit events (100+ types), longest platform retention option via customer storage, most certifications (12+ frameworks), and column-level lineage.

**Microsoft Fabric scores 4-4.7/5** reflecting strong capabilities with specific limitations. RBAC scores 4/5 losing 0.5 for OneLake Security preview status, 0.3 for workspace override architectural issue, and 0.2 for limited custom workspace roles. Reproducibility scores 4.5/5 leading in environment management (5/5 for Deployment Pipelines) but with dependency management and IaC less mature than Databricks. Collaboration scores 4.8/5 tied with Databricks for different reasons—excelling in real-time development collaboration and Power BI embedding while lacking open data sharing protocols. Auditability scores 4.7/5 with longest retention (9 years) and excellent Purview integration but fewer certifications than Databricks.

**Keboola scores 2.5-4/5** varying significantly by metric. RBAC scores 2.5/5 with fundamental granularity limitation (-2.0 for no table/row/column security), no custom roles (-0.5), no SCIM/JIT (-0.5), and manual provisioning not scaling (-0.5). Reproducibility scores 3.5/5 with adequate capabilities but CLI-driven approach requiring more manual setup, community-only Terraform provider (-2.0 compared to official providers), though virtual branching (4/5) and automatic lineage with OpenLineage (4.5/5) provide bright spots. Collaboration scores 2.5/5 with complete absence of real-time features (1/5), adequate internal Data Catalog sharing (4/5 for live data), but limited external sharing (2/5) and no modern collaboration infrastructure. Auditability scores 4/5 with good operational coverage, excellent automatic lineage, essential certifications, but limited retention (7 days Snowflake) compared to Fabric/Databricks.

## Conclusion

This comprehensive technical analysis reveals **Databricks as the enterprise leader** scoring consistently 4.8-5/5 across all metrics through Unity Catalog governance, unique ABAC capabilities, most mature Terraform provider, Delta Sharing open protocol, comprehensive audit logging (100+ action types), industry-leading certifications (12+ frameworks), and automatic column-level lineage. The platform suits large enterprises over 500 users, regulated industries requiring HIPAA/SOX/FedRAMP compliance, multi-cloud deployments, complex data classification, and organizations prioritizing open protocols for data sharing.

**Microsoft Fabric emerges as the Microsoft ecosystem champion** scoring 4-4.7/5 with strengths in real-time collaboration (co-editing with presence), superior environment management (Deployment Pipelines), longest audit retention (9 years), native Entra ID/Purview integration, and comprehensive Power BI embedding. Architectural limitations include workspace override bypassing OneLake RBAC, OneLake Security preview status, and proprietary sharing mechanisms. The platform optimally serves Microsoft-centric organizations with Azure/M365 investment, medium enterprises 100-500 users, single-cloud Azure deployments, and teams prioritizing developer collaboration over cross-platform data sharing.

**Keboola provides basic capabilities** scoring 2.5-4/5 with adequate features for small teams under 50 users working with non-sensitive data. Strengths include automatic lineage with OpenLineage standard, live Data Catalog sharing, and virtual branching, but fundamental limitations of bucket-level security (no table/row/column controls), seven predefined roles without customization, no SCIM/JIT provisioning, no real-time collaboration, and community-only Terraform provider make the platform **unsuitable for enterprises, regulated industries, or sensitive data**. Keboola serves startups, small teams with simple ETL/ELT, budget constraints, and minimal compliance requirements.

For master's thesis methodology, the most significant finding is **ABAC representing the future of data governance**—Databricks' ability to define security policies once based on data attributes (tags) and have them automatically apply to all matching objects across the entire data platform represents a paradigm shift from table-by-table RBAC configuration. The architectural constraint in Microsoft Fabric where workspace Admin/Member/Contributor bypass OneLake RBAC reveals the importance of security model design in platform selection. Keboola's bucket-level granularity demonstrates how fundamental security architecture decisions create permanent limitations that cannot be overcome through feature additions. These technical differentiators provide strong evidence for scoring justification and practical guidance for DataOps platform selection in enterprise contexts.