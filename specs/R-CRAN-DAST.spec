%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DAST
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Disaggregation for Maps with Changing Areal Boundaries

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-aghq 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-disaggregation 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-rSPDE 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sparseMVN 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-aghq 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-disaggregation 
Requires:         R-CRAN-fmesher 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-rSPDE 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sparseMVN 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-TMB 

%description
Tools for spatio-temporal disaggregation of areal data across multiple
time points, including support for changing polygon boundaries. Implements
methods for spatially aggregated log-Gaussian Cox process models with
changing areal boundaries as described in Ripstein, Brown and Stafford
(2026) "Spatio-Temporal Disaggregation with Changing Areal Boundaries"
<doi:10.48550/arXiv.2606.25074>. Combines polygon-level observations,
population rasters and optional covariate rasters to infer fine-scale
spatial fields over time. Models can be efficiently fit using 'TMB'
(Template Model Builder) and adaptive Gauss-Hermite quadrature for fast
approximate inference or via 'tmbstan' for MCMC.

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
