%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PFCI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Fast Causal Inference for High-Dimensional Structure Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-glasso 
Requires:         R-methods 

%description
Implements Penalized Fast Causal Inference (PFCI), a two-stage causal
structure learning procedure for high-dimensional settings with potential
latent variables and selection bias. In the first stage, neighborhood
selection via the Lasso constructs a sparse undirected skeleton. In the
second stage, the Fast Causal Inference (FCI) algorithm orients edges on
this reduced graph, producing a Partial Ancestral Graph (PAG) that
accounts for latent confounders. The method is consistent under sparsity
assumptions and substantially faster than standard FCI and RFCI in high
dimensions. See Pal, Ghosh, and Yang (2025)
<doi:10.48550/arXiv.2507.00173> for the underlying theory.

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
