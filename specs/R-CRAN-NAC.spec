%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NAC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Network-Adjusted Covariates for Community Detection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.2.0
Requires:         R-core >= 4.2.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-pracma 

%description
Incorporating node-level covariates for community detection has gained
increasing attention these years. This package provides the function for
implementing the novel community detection algorithm known as
Network-Adjusted Covariates for Community Detection (NAC), which is
designed to detect latent community structure in graphs with node-level
information, i.e., covariates. This algorithm can handle models such as
the degree-corrected stochastic block model (DCSBM) with covariates. NAC
specifically addresses the discrepancy between the community structure
inferred from the adjacency information and the community structure
inferred from the covariates information. For more detailed information,
please refer to the reference paper: Yaofang Hu and Wanjie Wang (2023)
<arXiv:2306.15616>. In addition to NAC, this package includes several
other existing community detection algorithms that are compared to NAC in
the reference paper. These algorithms are Spectral Clustering On Ratios-of
Eigenvectors (SCORE), network-based regularized spectral clustering
(Net-based), covariate-based spectral clustering (Cov-based),
covariate-assisted spectral clustering (CAclustering) and semidefinite
programming (SDP).

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
