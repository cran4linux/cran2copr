%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  treestats
%global packver   1.70.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.70.8
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Tree Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-treebalance 
BuildRequires:    R-CRAN-DDD 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-treebalance 
Requires:         R-CRAN-DDD 

%description
Collection of phylogenetic tree statistics, collected throughout the
literature. All functions have been written to maximize computation speed.
The package includes umbrella functions to calculate all statistics, all
balance associated statistics, or all branching time related statistics.
Furthermore, the 'treestats' package supports summary statistic
calculations on Ltables, provides speed-improved coding of branching
times, Ltable conversion and includes algorithms to create intermediately
balanced trees. Full description can be found in Janzen (2024)
<doi:10.1016/j.ympev.2024.108168>.

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
