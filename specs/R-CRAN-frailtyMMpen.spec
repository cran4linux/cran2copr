%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frailtyMMpen
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Algorithm for High-Dimensional Frailty Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-survival 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mgcv 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
The penalized and non-penalized Minorize-Maximization (MM) method for
frailty models to fit the clustered data, multi-event data and recurrent
data. Least absolute shrinkage and selection operator (LASSO), minimax
concave penalty (MCP) and smoothly clipped absolute deviation (SCAD)
penalized functions are implemented. All the methods are computationally
efficient. These general methods are proposed based on the following
papers, Huang, Xu and Zhou (2022) <doi:10.3390/math10040538>, Huang, Xu
and Zhou (2023) <doi:10.1177/09622802221133554>.

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
