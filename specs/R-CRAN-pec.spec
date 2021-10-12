%global __brp_check_rpaths %{nil}
%global packname  pec
%global packver   2021.10.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2021.10.11
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction Error Curves for Risk Prediction Models in Survival Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-rms >= 4.2.0
BuildRequires:    R-CRAN-riskRegression >= 2020.02.05
BuildRequires:    R-CRAN-survival >= 2.37.7
BuildRequires:    R-CRAN-timereg >= 1.8.9
BuildRequires:    R-CRAN-prodlim >= 1.4.9
BuildRequires:    R-CRAN-foreach >= 1.4.2
BuildRequires:    R-CRAN-lava >= 1.4.1
Requires:         R-CRAN-rms >= 4.2.0
Requires:         R-CRAN-riskRegression >= 2020.02.05
Requires:         R-CRAN-survival >= 2.37.7
Requires:         R-CRAN-timereg >= 1.8.9
Requires:         R-CRAN-prodlim >= 1.4.9
Requires:         R-CRAN-foreach >= 1.4.2
Requires:         R-CRAN-lava >= 1.4.1

%description
Validation of risk predictions obtained from survival models and competing
risk models based on censored data using inverse weighting and
cross-validation. Most of the 'pec' functionality has been moved to
'riskRegression'.

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
