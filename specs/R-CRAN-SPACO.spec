%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SPACO
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Component Analysis for Spatial Sequencing Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.3
Requires:         R-core >= 4.2.3
BuildRequires:    R-CRAN-Seurat >= 5.3.0
BuildRequires:    R-CRAN-Matrix >= 1.5
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Seurat >= 5.3.0
Requires:         R-CRAN-Matrix >= 1.5
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggforce 
Requires:         R-methods 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-scales 

%description
Spatial components offer tools for dimension reduction and spatially
variable gene detection for high dimensional spatial transcriptomics data.
Construction of a projection onto low-dimensional feature space of
spatially dependent metagenes offers pre-processing to clustering, testing
for spatial variability and denoising of spatial expression patterns. For
more details, see Koehler et al. (2026)
<doi:10.1093/bioinformatics/btag052>.

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
