%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gaselect
%global packver   1.0.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.25
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic Algorithm (GA) for Variable Selection from High-Dimensional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-methods >= 2.10.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.800.4
BuildRequires:    R-CRAN-Rcpp >= 0.10.5
Requires:         R-methods >= 2.10.0
Requires:         R-CRAN-Rcpp >= 0.10.5

%description
Provides a genetic algorithm for finding variable subsets in high
dimensional data with high prediction performance. The genetic algorithm
can use ordinary least squares (OLS) regression models or partial least
squares (PLS) regression models to evaluate the prediction power of
variable subsets. By supporting different cross-validation schemes, the
user can fine-tune the tradeoff between speed and quality of the solution.

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
