%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ACRER
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Accessibility for Recreation in R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-pivottabler 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-pivottabler 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pracma 

%description
Recreation model that simulates household types, group types, expected
visiting duration, and total visits from city zip codes to surrounding
destination areas. The methodology is based on the accessibility model
described in Bervaes et al. (1996) "Een model voor het gebruik van de
groene ruimte in stadslandschappen (Fase I)"
<https://www.wur.nl/en/library>, with optimization procedures based on
Goldfarb and Idnani (1983) <doi:10.1007/BF02591962> and Vanderbei et al.
(1986) <doi:10.1007/BF01840454>.

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
