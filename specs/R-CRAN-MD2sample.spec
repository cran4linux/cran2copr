%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MD2sample
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Various Methods for the Two Sample Problem in D>1 Dimensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-gTests 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lsa 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Ball 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-gTests 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lsa 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Ball 

%description
The routine twosample_test() in this package runs the two-sample test
using various test statistic for multivariate data. The user can also run
several tests and then find a p value adjusted for simultaneous inference.
The p values are found via permutation or via the parametric bootstrap.
The routine twosample_power() allows the estimation of the power of the
tests. The routine run.studies() allows a user to quickly study the power
of a new method and how it compares to those included in the package. For
details of the methods and references see the included vignettes.

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
