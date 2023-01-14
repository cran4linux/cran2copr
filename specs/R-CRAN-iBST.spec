%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iBST
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Improper Bagging Survival Tree

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rpart 
Requires:         R-parallel 

%description
Fit a full or subsampling bagging survival tree on a mixture of population
(susceptible and nonsusceptible) using either a pseudo R2 criterion or an
adjusted Logrank criterion. The predictor is evaluated using the Out Of
Bag Integrated Brier Score (IBS) and several scores of importance are
computed for variable selection. The thresholds values for variable
selection are computed using a nonparametric permutation test. See
'Cyprien Mbogning' and 'Philippe Broet'
(2016)<doi:10.1186/s12859-016-1090-x> for an overview about the methods
implemented in this package.

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
