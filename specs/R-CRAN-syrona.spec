%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  syrona
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stratified Prevalence Comparison Across OMOP CDM Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 6.0.0
BuildRequires:    R-CRAN-dbplyr >= 2.3.0
BuildRequires:    R-CRAN-CDMConnector >= 2.0.0
BuildRequires:    R-CRAN-readr >= 2.0.0
BuildRequires:    R-CRAN-omopgenerics >= 1.3.0
BuildRequires:    R-CRAN-DBI >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-meta >= 6.0.0
Requires:         R-CRAN-dbplyr >= 2.3.0
Requires:         R-CRAN-CDMConnector >= 2.0.0
Requires:         R-CRAN-readr >= 2.0.0
Requires:         R-CRAN-omopgenerics >= 1.3.0
Requires:         R-CRAN-DBI >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Derives stratified prevalence tables from the condition, procedure, and
drug records in OMOP CDM (Observational Medical Outcomes Partnership
Common Data Model) databases, computes log2 prevalence ratios between
paired datasets, and synthesizes them via random-effects meta-analysis at
multiple aggregation levels (year, age group, and sex). Between-study
variance is estimated with the Paule-Mandel method, as described in Paule
and Mandel (1982) <doi:10.6028/jres.087.022>.

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
