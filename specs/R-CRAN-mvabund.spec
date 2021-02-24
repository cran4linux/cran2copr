%global packname  mvabund
%global packver   4.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Analysing Multivariate Abundance Data

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tweedie 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-tweedie 
Requires:         R-CRAN-statmod 
Requires:         R-parallel 

%description
A set of tools for displaying, modeling and analysing multivariate
abundance data in community ecology. See 'mvabund-package.Rd' for details
of overall package organization. The package is implemented with the Gnu
Scientific Library (<http://www.gnu.org/software/gsl/>) and 'Rcpp'
(<http://dirk.eddelbuettel.com/code/rcpp.html>) 'R' / 'C++' classes.

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
