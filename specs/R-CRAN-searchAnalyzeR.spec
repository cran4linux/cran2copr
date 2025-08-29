%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  searchAnalyzeR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Analytics and Testing Framework for Systematic Review Search Strategies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.5
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-lubridate >= 1.9.0
BuildRequires:    R-CRAN-stringdist >= 0.9.10
BuildRequires:    R-CRAN-digest >= 0.6.31
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-openxlsx >= 4.2.5
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-lubridate >= 1.9.0
Requires:         R-CRAN-stringdist >= 0.9.10
Requires:         R-CRAN-digest >= 0.6.31
Requires:         R-stats 
Requires:         R-utils 

%description
Provides comprehensive analytics, reporting, and testing capabilities for
systematic review search strategies. The package focuses on validating
search performance, generating standardized 'PRISMA'-compliant reports,
and ensuring reproducibility in evidence synthesis. Features include
precision-recall analysis, cross-database performance comparison,
benchmark validation against gold standards, sensitivity analysis,
temporal coverage assessment, automated report generation, and statistical
comparison of search strategies. Supports multiple export formats
including 'CSV', 'Excel', 'RIS', 'BibTeX', and 'EndNote'. Includes tools
for duplicate detection, search strategy optimization, cross-validation
frameworks, meta-analysis of benchmark results, power analysis for study
design, and reproducibility package creation. Optionally connects to
'PubMed' for direct database searching and real-time strategy comparison
using the 'E-utilities' 'API'. Enhanced with bootstrap comparison methods,
'McNemar' test for strategy evaluation, and comprehensive visualization
tools for performance assessment. Methods based on Manning et al. (2008)
for information retrieval metrics, Moher et al. (2009) for 'PRISMA'
guidelines, and Sampson et al. (2006) for systematic review search
methodology.

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
