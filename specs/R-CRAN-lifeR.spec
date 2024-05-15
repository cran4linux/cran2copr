%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lifeR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Identify Sites for Your Bird List

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-rmarkdown >= 2.7
BuildRequires:    R-CRAN-terra >= 1.7.55
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.31
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-maptiles >= 0.6.1
BuildRequires:    R-CRAN-tidyterra >= 0.5.0
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-rmarkdown >= 2.7
Requires:         R-CRAN-terra >= 1.7.55
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-knitr >= 1.31
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-maptiles >= 0.6.1
Requires:         R-CRAN-tidyterra >= 0.5.0

%description
A suite of tools to use the 'eBird' database (<https://ebird.org/home/>)
and APIs to compare users' species lists to recent observations and create
a report of the top sites to visit to see new species.

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
