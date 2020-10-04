%global packname  Rphylopars
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}%{?buildtag}
Summary:          Phylogenetic Comparative Tools for Missing Data andWithin-Species Variation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-phylolm 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-phylolm 
Requires:         R-CRAN-phytools 
Requires:         R-Matrix 
Requires:         R-MASS 

%description
Tools for performing phylogenetic comparative methods for datasets with
with multiple observations per species (intraspecific variation or
measurement error) and/or missing data. Performs ancestral state
reconstruction and missing data imputation on the estimated evolutionary
model, which can be specified as Brownian Motion, Ornstein-Uhlenbeck,
Early-Burst, Pagel's lambda, kappa, or delta, or a star phylogeny.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
