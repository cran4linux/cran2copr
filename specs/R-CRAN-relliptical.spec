%global __brp_check_rpaths %{nil}
%global packname  relliptical
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Truncated Elliptical Family of Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-FuzzyNumbers.Ext.2 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Ryacas0 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-FuzzyNumbers.Ext.2 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppNumerical 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Ryacas0 
Requires:         R-stats 

%description
It generates random numbers from a truncated multivariate elliptical
distribution such as Normal, Student-t, Pearson VII, Slash, Logistic, and
others by specifying the density generating function. It also computes
first and second moment for some particular distributions.

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
