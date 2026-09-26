%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DCC
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Cleaning Center for Survey and Assessment Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-haven >= 2.5.5
BuildRequires:    R-CRAN-readODS >= 2.3.5
BuildRequires:    R-CRAN-stringi >= 1.7.0
BuildRequires:    R-CRAN-readxl >= 1.5.0
BuildRequires:    R-CRAN-openxlsx2 >= 1.28
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-haven >= 2.5.5
Requires:         R-CRAN-readODS >= 2.3.5
Requires:         R-CRAN-stringi >= 1.7.0
Requires:         R-CRAN-readxl >= 1.5.0
Requires:         R-CRAN-openxlsx2 >= 1.28
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-yaml 

%description
Rule-driven, auditable cleaning of survey and assessment response data,
implementing the WeianData Detect-Execute-Report workflow. Provides a
multi-format, multi-encoding input layer (CSV, 'Excel', 'SPSS', 'Stata',
'SAS', Parquet, JSON), the dcc_data container with a provenance chain,
level-0 structural diagnostics, five built-in response-quality detectors
(missing items, straight-lining, response time, trap items, score
anomalies), a declarative YAML rule engine, an execution engine with a
cell-level audit log, answer-key scoring, multi-form to master item bank
mapping, a normalized report model rendered as bilingual staff workbooks
and HTML, complete statistical bundles, and versioned machine JSON/JSONL
with findings-to-changes reconciliation, cell-level lineage tracing, and
manifest-based one-command reproduction. Includes a protected bilingual
strict project workbook and matching JSON contract with cell-addressed
validation, non-mutating preflight, preview-first execution, and localized
staff guidance. All formally supported input backends install with the
package; PDF is optional rather than a fixed report output.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
