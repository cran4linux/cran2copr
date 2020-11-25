%global packname  chickn
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          'Compressive' Hierarchical Kernel Clustering Toolbox

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-bigstatsr >= 1.2.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-zipfR 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rmio 
Requires:         R-CRAN-bigstatsr >= 1.2.3
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-zipfR 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Rdpack 

%description
Routines for efficient cluster analysis of large scale data. This package
implements the 'CHICKN' clustering algorithm (see 'Permiakova' 'et' 'al.'
(2020) "'CHICKN': Extraction of 'peptide' 'chromatographic' 'elution'
profiles from large scale mass 'spectrometry' data by means of
'Wasserstein' 'compressive' hierarchical cluster analysis"). Functions for
data compression, hierarchical clustering and post processing are
provided.

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
