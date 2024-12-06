%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pomdp
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Infrastructure for Partially Observable Markov Decision Processes (POMDP)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-pomdpSolve >= 1.0.4
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-pomdpSolve >= 1.0.4
Requires:         R-CRAN-processx 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-igraph 

%description
Provides the infrastructure to define and analyze the solutions of
Partially Observable Markov Decision Process (POMDP) models. Interfaces
for various exact and approximate solution algorithms are available
including value iteration, point-based value iteration and SARSOP.
Smallwood and Sondik (1973) <doi:10.1287/opre.21.5.1071>.

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
