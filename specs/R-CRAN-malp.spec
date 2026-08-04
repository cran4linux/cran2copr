%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  malp
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Agreement Linear Prediction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-boot 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 
Requires:         R-graphics 
Requires:         R-CRAN-boot 

%description
Provides tools for estimation and prediction using Maximum Agreement
Linear Predictors (MALPs). MALPs provide an alternative to least squares
linear predictors when agreement between predicted and observed values, as
measured by Lin's Concordance Correlation Coefficient (CCC), is of primary
interest. Applications include missing value imputation and calibration
studies. The package includes functions for model estimation, prediction,
statistical inference, cross-validation, and model diagnostics. The
implemented methodology is described in Kim et al. (2026)
<doi:10.1214/26-EJS2550>.

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
