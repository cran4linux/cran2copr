%global __brp_check_rpaths %{nil}
%global packname  locpolExpectile
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Local Polynomial Expectile Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-locpol 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-expectreg 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-lestat 
Requires:         R-CRAN-locpol 
Requires:         R-stats 
Requires:         R-CRAN-expectreg 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-lestat 

%description
Provides the local polynomial expectile regression method and different
bandwidth selection procedures. The codes include local polynomial
univariate expectile regression with several data-driven methods for
bandwidth selection; local linear bivariate and trivariate expectile
regression; and partially linear expectile regression, allowing for
different errors structures (homoscedastic error and various
heteroscedastic error structures). For more details, see Adam and Gijbels
(2021a) <doi:10.1007/s10463-021-00799-y> and Adam and Gijbels (2021b)
<doi:10.1007/978-3-030-73249-3_8>.

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
