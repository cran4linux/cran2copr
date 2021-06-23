%global __brp_check_rpaths %{nil}
%global packname  GFisher
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Fisher's Combination Tests Under Dependence

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 

%description
Accurate and computationally efficient p-value calculation methods for a
general family of Fisher type statistics (GFisher). The GFisher covers
Fisher's combination, Good's statistic, Lancaster's statistic, weighted
Z-score combination, etc. It allows a flexible weighting scheme, as well
as an omnibus procedure that automatically adapts proper weights and
degrees of freedom to a given data. The new p-value calculation methods
are based on novel ideas of moment-ratio matching and joint-distribution
approximation. The technical details can be found in Hong Zhang and
Zheyang Wu (2020) <arXiv:2003.01286>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
