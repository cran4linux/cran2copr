%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CommEcol
%global packver   1.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Community Ecology Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-rncl 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-adespatial 
BuildRequires:    R-CRAN-betapart 
BuildRequires:    R-CRAN-gmp 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-rncl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-adespatial 
Requires:         R-CRAN-betapart 
Requires:         R-CRAN-gmp 

%description
Autosimilarity curves, standardization of spatial extent, dissimilarity
indexes that overweight rare species, phylogenetic and functional
(pairwise and multisample) dissimilarity indexes and nestedness for
phylogenetic, functional and other diversity metrics. The methods for
phylogenetic and functional nestedness is described in Melo, Cianciaruso
and Almeida-Neto (2014) <doi:10.1111/2041-210X.12185>. This should be a
complement to available packages, particularly 'vegan'.

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
