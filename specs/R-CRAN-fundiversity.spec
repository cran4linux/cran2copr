%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fundiversity
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Computation of Alpha Functional Diversity Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-vegan 

%description
Computes 5 alpha-functional diversity indices: Functional Divergence
(FDiv), Function Evenness (FEve), Functional Richness (FRic), Functional
Dispersion (FDis) and Rao's entropy (Q) (reviewed in Villéger et al. 2008
<doi:10.1890/07-1206.1>). Provides efficient, modular, and parallel
functions to compute functional diversity indices.

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
