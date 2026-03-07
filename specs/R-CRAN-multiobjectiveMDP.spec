%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiobjectiveMDP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Solution Methods for Multi-Objective Markov Decision Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-linprog 
BuildRequires:    R-CRAN-lintools 
BuildRequires:    R-CRAN-nsga2R 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-linprog 
Requires:         R-CRAN-lintools 
Requires:         R-CRAN-nsga2R 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-prodlim 
Requires:         R-stats 

%description
Compendium of the most representative algorithms in print---vector-valued
dynamic programming, linear programming, policy iteration, the weighting
factor approach---for solving multi-objective Markov decision processes,
with or without reward discount, over a finite or infinite horizon.
Mifrani, A. (2024) <doi:10.1007/s10479-024-06439-x>; Mifrani, A. & Noll,
D. <doi:10.48550/arXiv.2502.13697>; Wakuta, K. (1995)
<doi:10.1016/0304-4149(94)00064-Z>.

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
