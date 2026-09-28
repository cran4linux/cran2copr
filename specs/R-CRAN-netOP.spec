%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netOP
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Network Data Operations and Overlapping Partitions Based Methods for Large Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-tibble 

%description
Implements methods for generating, embedding, and clustering random
networks and for estimating and selecting statistical network models.
Provides SONNET (Subsampling ON NETwork), a scalable subsampling-based
divide-and-conquer method for community detection described by
Chakrabarty, Sengupta and Chen (2025) <doi:10.5705/ss.202022.0108>, and
NETCROP (NETwork CRoss-validation using Overlapping Partitions), an
overlapping-partition framework for network cross-validation, model
selection, and regularization tuning described by Chakrabarty, Sengupta
and Chen (2026) <doi:10.48550/arXiv.2504.06903>. Also includes spectral
and latent-space methods, loss functions, and helper functions for
statistical analysis of network data.

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
