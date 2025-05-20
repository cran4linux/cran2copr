%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sfclust
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatial Functional Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cubelyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-cubelyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 

%description
Bayesian clustering of spatial regions with similar functional shapes
using spanning trees and latent Gaussian models. The method enforces
spatial contiguity within clusters and supports a wide range of latent
Gaussian models, including non-Gaussian likelihoods, via the R-INLA
framework. The algorithm is based on Zhong, R., Chacón-Montalván, E. A.,
and Moraga, P. (2024) <doi:10.48550/arXiv.2407.12633>, extending the
approach of Zhang, B., Sang, H., Luo, Z. T., and Huang, H. (2023)
<doi:10.1214/22-AOAS1643>. The package includes tools for model fitting,
convergence diagnostics, visualization, and summarization of clustering
results.

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
