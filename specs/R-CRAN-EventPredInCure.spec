%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EventPredInCure
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Event Prediction Including Cured Population

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-CRAN-plotly >= 4.10.1
BuildRequires:    R-utils >= 4.1.2
BuildRequires:    R-splines >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-survival >= 2.41.3
BuildRequires:    R-CRAN-flexsurv >= 2.2.2
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-msm >= 1.7.0
BuildRequires:    R-CRAN-rstpm2 >= 1.6.1
BuildRequires:    R-CRAN-Matrix >= 1.2.14
BuildRequires:    R-CRAN-mvtnorm >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-perm >= 1.0.0.2
BuildRequires:    R-CRAN-erify >= 0.4.0
BuildRequires:    R-CRAN-MLEcens >= 0.1.7
BuildRequires:    R-CRAN-KMsurv >= 0.1.5
BuildRequires:    R-CRAN-tmvtnsim >= 0.1.3
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-CRAN-plotly >= 4.10.1
Requires:         R-utils >= 4.1.2
Requires:         R-splines >= 3.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-survival >= 2.41.3
Requires:         R-CRAN-flexsurv >= 2.2.2
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-msm >= 1.7.0
Requires:         R-CRAN-rstpm2 >= 1.6.1
Requires:         R-CRAN-Matrix >= 1.2.14
Requires:         R-CRAN-mvtnorm >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-perm >= 1.0.0.2
Requires:         R-CRAN-erify >= 0.4.0
Requires:         R-CRAN-MLEcens >= 0.1.7
Requires:         R-CRAN-KMsurv >= 0.1.5
Requires:         R-CRAN-tmvtnsim >= 0.1.3

%description
Predicts enrollment and events assumed enrollment and treatment-specific
time-to-event models, and calculates test statistics for time-to-event
data with cured population based on the simulation.Methods for prediction
event in the existence of cured population are as described in : Chen,
Tai-Tsang(2016) <doi:10.1186/s12874-016-0117-3>.

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
