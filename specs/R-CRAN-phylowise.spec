%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phylowise
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Pairwise Contrasts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-BMA 
BuildRequires:    R-CRAN-phylotate 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-BMA 
Requires:         R-CRAN-phylotate 
Requires:         R-CRAN-Rcpp 

%description
A phylogenetic comparative method for finding associations between
biological traits and molecular evolutionary rates. The method samples
pairs from a phylogeny such that each pair has non-overlapping edge paths,
and can therefore be treated as statistically independent observations.
Linear regression is performed on the pair contrasts. This approach is
similar to phylogenetically independent contrasts (PIC) but without
reconstructing the traits at internal nodes, and is better suited for
finding trait-rate associations than phylogenetic generalised least
squares (PGLS). Refer to Douglas and Bromham (2026)
<doi:10.64898/2026.08.13.744736> for further details.

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
