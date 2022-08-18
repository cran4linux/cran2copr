%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dyads
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dyadic Network Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-CholWishart 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppZiggurat 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-CholWishart 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RcppZiggurat 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-mvtnorm 

%description
Contains functions for the MCMC simulation of dyadic network models j2
(Zijlstra, 2017, <doi:10.1080/0022250X.2017.1387858>) and p2 (Van Duijn,
Snijders & Zijlstra, 2004, <doi: 10.1046/j.0039-0402.2003.00258.x>), the
multilevel p2 model (Zijlstra, Van Duijn & Snijders (2009) <doi:
10.1348/000711007X255336>), and the bidirectional (multilevel) counterpart
of the the multilevel p2 model as described in Zijlstra, Van Duijn &
Snijders (2009) <doi: 10.1348/000711007X255336>, the (multilevel) b2
model.

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
