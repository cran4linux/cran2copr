%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cudaverse
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight 'CUDA' Numerical Computing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 

%description
Provides a lightweight interface to graphics processing unit
(GPU)-accelerated numerical computing using 'CUDA'. Dense tensors, sparse
matrices, decompositions, distances, exact nearest neighbours, clustering,
graph workflows, and embeddings share one consistent interface. The native
backend discovers the 'NVIDIA CUDA Driver API', 'cuBLAS', and 'cuSOLVER'
libraries at runtime without bundling 'LibTorch' or the 'CUDA Runtime'.
Stage-level provenance records the backend, device, and data transfers
used by each result. A portable implementation supports package validation
on systems without 'CUDA'. Background for the included Leiden community
detection and uniform manifold approximation and projection methods is
given by Traag, Waltman and van Eck (2019)
<doi:10.1038/s41598-019-41695-z> and McInnes et al. (2018)
<doi:10.21105/joss.00861>, respectively.

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
