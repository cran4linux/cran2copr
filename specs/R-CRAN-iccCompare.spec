%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iccCompare
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comparison of Dependent Intraclass Correlation Coefficients

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-mvtnorm 

%description
Provides methods for testing the equality of dependent intraclass
correlation coefficients (ICCs) estimated using linear mixed-effects
models. Several of the implemented approaches are based on the work of
Donner and Zou (2002) <doi:10.1111/1467-9884.00324>.

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
