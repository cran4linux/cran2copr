%global __brp_check_rpaths %{nil}
%global packname  MLVSBM
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Stochastic Block Model for Multilevel Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-blockmodels 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-cluster 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-blockmodels 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-cluster 

%description
Simulation, inference and clustering of multilevel networks using a
Stochastic Block Model framework as described in Chabert-Liddell,
Barbillon, Donnet and Lazega (2021) <doi:10.1016/j.csda.2021.107179>. A
multilevel network is defined as the junction of two interaction networks,
the upper level or inter-organizational level and the lower level or
inter-individual level. The inter-level represents an affiliation
relationship.

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
