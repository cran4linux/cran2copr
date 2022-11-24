%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TransTGGM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transfer Learning for Tensor Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-Tlasso 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-expm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-Tlasso 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-expm 

%description
Tensor Gaussian graphical models (GGMs) have important applications in
numerous areas, which can interpret conditional independence structures
within tensor data. Yet, the available tensor data in one single study is
often limited due to high acquisition costs. Although relevant studies can
provide additional data, it remains an open question how to pool such
heterogeneous data. This package implements a transfer learning framework
for tensor GGMs, which takes full advantage of informative auxiliary
domains even when non-informative auxiliary domains are present,
benefiting from the carefully designed data-adaptive weights. Reference:
Ren, M., Zhen Y., and Wang J. (2022). "Transfer learning for tensor
graphical models" <arXiv:2211.09391>.

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
