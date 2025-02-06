%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DAISIE
%global packver   4.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamical Assembly of Islands by Speciation, Immigration and Extinction

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-DDD >= 5.0
BuildRequires:    R-CRAN-BH >= 1.81.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-DDD >= 5.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-deSolve 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-subplex 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 

%description
Simulates and computes the (maximum) likelihood of a dynamical model of
island biota assembly through speciation, immigration and extinction. See
Valente et al. (2015) <doi:10.1111/ele.12461>.

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
