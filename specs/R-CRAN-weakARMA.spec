%global __brp_check_rpaths %{nil}
%global packname  weakARMA
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for the Analysis of Weak ARMA Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-CRAN-vars >= 1.5.6
BuildRequires:    R-CRAN-CompQuadForm >= 1.4.3
BuildRequires:    R-CRAN-matrixStats >= 0.61
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-CRAN-vars >= 1.5.6
Requires:         R-CRAN-CompQuadForm >= 1.4.3
Requires:         R-CRAN-matrixStats >= 0.61

%description
Numerous time series admit autoregressive moving average (ARMA)
representations, in which the errors are uncorrelated but not necessarily
independent. These models are called weak ARMA by opposition to the
standard ARMA models, also called strong ARMA models, in which the error
terms are supposed to be independent and identically distributed (iid).
This package allows the study of nonlinear time series models through weak
ARMA representations. It determines identification, estimation and
validation for ARMA models and for AR and MA models in particular.
Functions can also be used in the strong case. This package also works on
white noises by omitting arguments 'p', 'q', 'ar' and 'ma'. See Francq, C.
and Zakoïan, J. (1998) <doi:10.1016/S0378-3758(97)00139-0> and Boubacar
Maïnassara, Y. and Saussereau, B. (2018)
<doi:10.1080/01621459.2017.1380030> for more details.

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
