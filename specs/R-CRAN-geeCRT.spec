%global packname  geeCRT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bias-Corrected GEE for Cluster Randomized Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-mvtnorm 

%description
Population-averaged models have been increasingly used in the design and
analysis of cluster randomized trials (CRTs). To facilitate the
applications of population-averaged models in CRTs, the package implements
the generalized estimating equations (GEE) and matrix-adjusted estimating
equations (MAEE) approaches to jointly estimate the marginal mean models
correlation models both for general CRTs and stepped wedge CRTs. Despite
the general GEE/MAEE approach, the package also implements a fast
cluster-period GEE method by Li et al. (2021)
<doi:10.1093/biostatistics/kxaa056> specifically for stepped wedge CRTs
with large and variable cluster-period sizes and gives a simple and
efficient estimating equations approach based on the cluster-period means
to estimate the intervention effects as well as correlation parameters. In
addition, the package also provides functions for generating correlated
binary data with specific mean vector and correlation matrix based on the
multivariate probit method in Emrich and Piedmonte (1991)
<doi:10.1080/00031305.1991.10475828> or the conditional linear family
method in Qaqish (2003) <doi:10.1093/biomet/90.2.455>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
