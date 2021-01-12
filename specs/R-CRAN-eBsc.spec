%global packname  eBsc
%global packver   4.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.13
Release:          1%{?dist}%{?buildtag}
Summary:          "Empirical Bayes Smoothing Splines with Correlated Errors"

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-parallel 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-splines 
Requires:         R-CRAN-Rcpp 

%description
Presents a statistical method that uses a recursive algorithm for signal
extraction. The method handles a non-parametric estimation for the
correlation of the errors. See "Serra", "Krivobokova" and "Rosales" (2018)
<arXiv:1812.06948> for details.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
