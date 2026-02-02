%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SVG
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially Variable Genes Detection Methods for Spatial Transcriptomics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-MASS 

%description
A unified framework for detecting spatially variable genes (SVGs) in
spatial transcriptomics data. This package integrates multiple
state-of-the-art SVG detection methods including 'MERINGUE' (Moran's I
based spatial autocorrelation), 'Giotto' binSpect (binary spatial
enrichment test), 'SPARK-X' (non-parametric kernel-based test), and
'nnSVG' (nearest-neighbor Gaussian processes). Each method is implemented
with optimized performance through vectorization, parallelization, and
'C++' acceleration where applicable. Methods are described in Miller et
al. (2021) <doi:10.1101/gr.271288.120>, Dries et al. (2021)
<doi:10.1186/s13059-021-02286-2>, Zhu et al. (2021)
<doi:10.1186/s13059-021-02404-0>, and Weber et al. (2023)
<doi:10.1038/s41467-023-39748-z>.

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
