%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  steppedwedge
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Data from Stepped Wedge Cluster Randomized Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-methods >= 3.6.2
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-geepack >= 1.3.12
BuildRequires:    R-CRAN-lme4 >= 1.1.35.5
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-performance >= 0.12.4
Requires:         R-stats >= 4.0.0
Requires:         R-methods >= 3.6.2
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-geepack >= 1.3.12
Requires:         R-CRAN-lme4 >= 1.1.35.5
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-performance >= 0.12.4

%description
Provide various functions and tools to help fit models for estimating
treatment effects in stepped wedge cluster randomized trials. Implements
methods described in Kenny, Voldal, Xia, and Heagerty (2022) "Analysis of
stepped wedge cluster randomized trials in the presence of a time-varying
treatment effect", <doi:10.1002/sim.9511>.

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
