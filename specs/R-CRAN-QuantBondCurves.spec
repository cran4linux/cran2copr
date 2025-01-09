%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuantBondCurves
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Bond Values and Interest Rate Curves for Finance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-quantdates 
BuildRequires:    R-CRAN-Rsolnp 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-quantdates 
Requires:         R-CRAN-Rsolnp 

%description
Values different types of assets and calibrates discount curves for
quantitative financial analysis. It covers fixed coupon assets, floating
note assets, interest and cross currency swaps with different payment
frequencies. Enables the calibration of spot, instantaneous forward and
basis curves, making it a powerful tool for accurate and flexible bond
valuation and curve generation. The valuation and calibration techniques
presented here are consistent with industry standards and incorporates
author's own calculations. Tuckman, B., Serrat, A. (2022, ISBN:
978-1-119-83555-4).

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
