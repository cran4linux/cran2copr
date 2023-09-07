%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  optimall
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Allocate Samples Among Strata

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-methods >= 4.0.0
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-rlang >= 0.2.2
Requires:         R-stats >= 4.0.2
Requires:         R-methods >= 4.0.0
Requires:         R-utils >= 3.5.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-rlang >= 0.2.2

%description
Functions for the design process of survey sampling, with specific tools
for multi-wave and multi-phase designs. Perform optimum allocation using
Neyman (1934) <doi:10.2307/2342192> or Wright (2012)
<doi:10.1080/00031305.2012.733679> allocation, split strata based on
quantiles or values of known variables, randomly select samples from
strata, allocate sampling waves iteratively, and organize a complex survey
design. Also includes a Shiny application for observing the effects of
different strata splits.

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
