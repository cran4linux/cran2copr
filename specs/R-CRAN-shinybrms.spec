%global packname  shinybrms
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical User Interface ('shiny' App) for 'brms'

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.19.3
BuildRequires:    R-CRAN-brms >= 2.14.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.19.3
Requires:         R-CRAN-brms >= 2.14.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-rstantools

%description
A graphical user interface (GUI) for fitting Bayesian regression models
using the package 'brms' which in turn relies on 'Stan'
(<https://mc-stan.org/>). The 'shinybrms' GUI is a 'shiny' app.

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
