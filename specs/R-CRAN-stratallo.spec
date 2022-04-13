%global __brp_check_rpaths %{nil}
%global packname  stratallo
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimum Sample Allocation in Stratified Sampling Schemes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-lifecycle 

%description
Functions in this package provide solution to classical problem in survey
methodology - an optimum sample allocation in stratified sampling schemes.
In this context, the optimal allocation is in the classical
Tschuprov-Neyman's sense and it satisfies additional either lower or upper
bounds restrictions imposed on sample sizes in strata. There are few
different algorithms available to use, and one them is based on popular
sample allocation method that applies Neyman allocation to recursively
reduced set of strata. A minor modification of the classical optimium
sample allocation problem leads to the minimum sample size allocation.
This problems lies in the determination of a vector of strata sample sizes
that minimizes total sample size, under assumed fixed level of the
pi-estimator's variance. As in the case of the classical optimal
allocation, the problem of minimum sample size allocation can be
complemented by imposing upper bounds constraints on sample sizes in
strata. A function that solves the minimum sample size allocation problem
is included in stratallo package.

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
