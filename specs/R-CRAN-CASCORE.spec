%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CASCORE
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate Assisted Spectral Clustering on Ratios of Eigenvectors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-pracma 

%description
Functions for implementing the novel algorithm CASCORE, which is designed
to detect latent community structure in graphs with node covariates. This
algorithm can handle models such as the covariate-assisted degree
corrected stochastic block model (CADCSBM). CASCORE specifically addresses
the disagreement between the community structure inferred from the
adjacency information and the community structure inferred from the
covariate information. For more detailed information, please refer to the
reference paper: Yaofang Hu and Wanjie Wang (2022) <arXiv:2306.15616>. In
addition to CASCORE, this package includes several classical community
detection algorithms that are compared to CASCORE in our paper. These
algorithms are: Spectral Clustering On Ratios-of Eigenvectors (SCORE),
normalized PCA, ordinary PCA, network-based clustering, covariates-based
clustering and covariate-assisted spectral clustering (CASC). By providing
these additional algorithms, the package enables users to compare their
performance with CASCORE in community detection tasks.

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
