%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JANE
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Just Another Latent Space Network Clustering Algorithm

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-aricode 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-utils 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-aricode 
Requires:         R-CRAN-stringdist 
Requires:         R-utils 
Requires:         R-splines 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Fit latent space network cluster models using an expectation-maximization
algorithm. Enables flexible modeling of unweighted or weighted network
data (with or without noise edges), supporting both directed and
undirected networks (with or without degree heterogeneity). Designed to
handle large networks efficiently, it allows users to explore network
structure through latent space representations, identify clusters (i.e.,
community detection) within network data, and simulate networks with
varying clustering, connectivity patterns, and noise edges. Methodology
for the implementation is described in Arakkal and Sewell (2025)
<doi:10.1016/j.csda.2025.108228>.

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
