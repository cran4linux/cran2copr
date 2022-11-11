%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  castor
%global packver   1.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Phylogenetics on Large Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-naturalsort 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-parallel 
Requires:         R-CRAN-naturalsort 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RSpectra 

%description
Efficient phylogenetic analyses on massive phylogenies comprising up to
millions of tips. Functions include pruning, rerooting, calculation of
most-recent common ancestors, calculating distances from the tree root and
calculating pairwise distances. Calculation of phylogenetic signal and
mean trait depth (trait conservatism), ancestral state reconstruction and
hidden character prediction of discrete characters, simulating and fitting
models of trait evolution, fitting and simulating diversification models,
dating trees, comparing trees, and reading/writing trees in Newick format.
Citation: Louca, Stilianos and Doebeli, Michael (2017)
<doi:10.1093/bioinformatics/btx701>.

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
