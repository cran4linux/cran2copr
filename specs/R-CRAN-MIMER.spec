%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MIMER
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Data Wrangling for Antimicrobial Resistance Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AMR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fuzzyjoin 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-AMR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fuzzyjoin 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 

%description
Designed for analyzing the Medical Information Mart for Intensive
Care(MIMIC) dataset, a repository of freely accessible electronic health
records. MIMER(MIMIC-enabled Research) package, offers a suite of data
wrangling functions tailored specifically for preparing the dataset for
research purposes, particularly in antimicrobial resistance(AMR) studies.
It simplifies complex data manipulation tasks, allowing researchers to
focus on their primary inquiries without being bogged down by wrangling
complexities.

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
