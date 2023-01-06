%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  welo
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted and Standard Elo Rates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-boot >= 1.3
BuildRequires:    R-CRAN-Rdpack >= 1.0
BuildRequires:    R-CRAN-rio >= 0.5.29
BuildRequires:    R-CRAN-xts >= 0.12.0
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-boot >= 1.3
Requires:         R-CRAN-Rdpack >= 1.0
Requires:         R-CRAN-rio >= 0.5.29
Requires:         R-CRAN-xts >= 0.12.0

%description
Estimates the standard and weighted Elo (WElo, Angelini et al., 2022
<doi:10.1016/j.ejor.2021.04.011>) rates. The current version provides Elo
and WElo rates for tennis, according to different systems of weights
(games or sets) and scale factors (constant, proportional to the number of
matches, with more weight on Grand Slam matches or matches played on a
specific surface). Moreover, the package gives the possibility of
estimating the (bootstrap) standard errors for the rates. Finally, the
package includes betting functions that automatically select the matches
on which place a bet.

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
