%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  radiant.basics
%global packver   1.6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Basics Menu for Radiant: Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-psych >= 1.8.3.3
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-radiant.data >= 1.6.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-import >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-patchwork >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-polycor >= 0.7.10
BuildRequires:    R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-psych >= 1.8.3.3
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-radiant.data >= 1.6.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-import >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-patchwork >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-polycor >= 0.7.10
Requires:         R-CRAN-scales >= 0.4.0

%description
The Radiant Basics menu includes interfaces for probability calculation,
central limit theorem simulation, comparing means and proportions,
goodness-of-fit testing, cross-tabs, and correlation. The application
extends the functionality in 'radiant.data'.

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
