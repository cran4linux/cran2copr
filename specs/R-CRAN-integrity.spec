%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  integrity
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing the Integrity and Trustworthiness of Clinical Trials Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-car 
Requires:         R-CRAN-rlang 

%description
The integrity package implements the IPD Integrity Tool, a structured and
transparent framework for evaluating the integrity of individual
participant data (IPD) from randomised trials (see Hunter et al. (2024)
<doi:10.1002/jrsm.1738> and <doi:10.32614/RJ-2017-008>). It supports users
to identify potential issues, such as unusual data patterns, implausible
values, lack of expected correlations, date violations, and
inconsistencies. The package provides reproducible workflows for
screening, documenting and summarising integrity concerns, and may be
applied by evidence synthesists, editors, and others to determine whether
a randomised trial may be considered sufficiently trustworthy to
contribute to the evidence base that informs policy and practice.

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
