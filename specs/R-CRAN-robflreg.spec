%global __brp_check_rpaths %{nil}
%global packname  robflreg
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Functional Linear Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-goffda 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-goffda 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-plot3D 

%description
Functions for implementing robust methods for functional linear
regression. In the functional linear regression, we consider
scalar-on-function linear regression and function-on-function linear
regression. More details, see Beyaztas, U., and Shang, H. L. (2021)
<arXiv:2111.01238> and Beyaztas, U., and Shang, H. L. (2022)
<arXiv:2203.05065>.

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
