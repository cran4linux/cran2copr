%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eventPred
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Event Prediction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.1
BuildRequires:    R-splines >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-survival >= 2.41.3
BuildRequires:    R-CRAN-flexsurv >= 2.2.2
BuildRequires:    R-CRAN-rstpm2 >= 1.6.1
BuildRequires:    R-CRAN-Matrix >= 1.2.14
BuildRequires:    R-CRAN-mvtnorm >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-erify >= 0.4.0
Requires:         R-CRAN-plotly >= 4.10.1
Requires:         R-splines >= 3.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-survival >= 2.41.3
Requires:         R-CRAN-flexsurv >= 2.2.2
Requires:         R-CRAN-rstpm2 >= 1.6.1
Requires:         R-CRAN-Matrix >= 1.2.14
Requires:         R-CRAN-mvtnorm >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-erify >= 0.4.0

%description
Predicts enrollment and events at the design or analysis stage using
specified enrollment and time-to-event models through simulations.

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
