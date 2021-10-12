%global __brp_check_rpaths %{nil}
%global packname  AgroReg
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Analysis Linear and Nonlinear for Agriculture

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rcompanion 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-egg 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-car 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rcompanion 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-egg 

%description
Linear and nonlinear regression analysis common in agricultural science
articles (Archontoulis & Miguez (2015). <doi:10.2134/agronj2012.0506>).
The package includes polynomial, exponential, gaussian, logistic,
logarithmic, segmented, non-parametric models, among others. The functions
return the model coefficients and their respective p values, coefficient
of determination, root mean square error, AIC, BIC, as well as graphs with
the equations automatically.

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
