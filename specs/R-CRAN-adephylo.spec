%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adephylo
%global packver   1.1-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.16
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Analyses for the Phylogenetic Comparative Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ade4 >= 1.7.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-adegenet 
Requires:         R-CRAN-ade4 >= 1.7.10
Requires:         R-methods 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-adegenet 

%description
Multivariate tools to analyze comparative data, i.e. a phylogeny and some
traits measured for each taxa. The package contains functions to represent
comparative data, compute phylogenetic proximities, perform multivariate
analysis with phylogenetic constraints and test for the presence of
phylogenetic autocorrelation. The package is described in Jombart et al
(2010) <doi:10.1093/bioinformatics/btq292>.

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
