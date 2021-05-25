%global packname  mortAAR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Archaeological Mortality Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-Rdpack >= 0.4.20
Requires:         R-methods >= 3.3.3
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-Rdpack >= 0.4.20

%description
A collection of functions for the analysis of archaeological mortality
data (on the topic see e.g. Chamberlain 2006
<https://books.google.de/books?id=nG5FoO_becAC&lpg=PA27&ots=LG0b_xrx6O&dq=life%%20table%%20archaeology&pg=PA27#v=onepage&q&f=false>).
It takes demographic data in different formats and displays the result in
a standard life table as well as plots the relevant indices (percentage of
deaths, survivorship, probability of death, life expectancy, percentage of
population).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
