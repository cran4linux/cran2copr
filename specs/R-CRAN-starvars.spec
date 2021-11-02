%global __brp_check_rpaths %{nil}
%global packname  starvars
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Vector Logistic Smooth Transition Models Estimation and Prediction

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lessR 
BuildRequires:    R-CRAN-quantmod 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-optimParallel 
Requires:         R-parallel 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lessR 
Requires:         R-CRAN-quantmod 

%description
Allows the user to estimate a vector logistic smooth transition
autoregressive model via maximum log-likelihood or nonlinear least
squares. It further permits to test for linearity in the multivariate
framework against a vector logistic smooth transition autoregressive model
with a single transition variable. The estimation method is discussed in
Terasvirta and Yang (2014, <doi:10.1108/S0731-9053(2013)0000031008>).
Also, realized covariances can be constructed from stock market prices or
returns, as explained in Andersen et al. (2001,
<doi:10.1016/S0304-405X(01)00055-1>).

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
