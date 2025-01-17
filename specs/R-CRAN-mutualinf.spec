%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mutualinf
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computation and Decomposition of the Mutual Information Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-runner 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-CRAN-runner 
Requires:         R-stats 

%description
The Mutual Information Index (M) introduced to social science literature
by Theil and Finizza (1971) <doi:10.1080/0022250X.1971.9989795> is a
multigroup segregation measure that is highly decomposable and that
according to Frankel and Volij (2011) <doi:10.1016/j.jet.2010.10.008> and
Mora and Ruiz-Castillo (2011) <doi:10.1111/j.1467-9531.2011.01237.x>
satisfies the Strong Unit Decomposability and Strong Group Decomposability
properties. This package allows computing and decomposing the total index
value into its "between" and "within" terms. These last terms can also be
decomposed into their contributions, either by group or unit
characteristics. The factors that produce each "within" term can also be
displayed at the user's request. The results can be computed considering a
variable or sets of variables that define separate clusters.

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
