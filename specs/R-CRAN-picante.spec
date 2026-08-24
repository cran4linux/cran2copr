%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  picante
%global packver   1.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          Integrating Phylogenies and Ecology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-nlme 
Requires:         R-methods 

%description
Functions for phylocom integration, community analyses, null-models,
traits and evolution. Implements numerous ecophylogenetic approaches
including measures of community phylogenetic and trait diversity,
phylogenetic signal, estimation of trait values for unobserved taxa, null
models for community and phylogeny randomizations, and utility functions
for data input/output and phylogeny plotting. A full description of
package functionality and methods are provided by Kembel et al. (2010)
<doi:10.1093/bioinformatics/btq166>.

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
