%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jlmerclusterperm
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster-Based Permutation Analysis for Densely Sampled Time Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-JuliaConnectoR 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-JuliaConnectoR 
Requires:         R-CRAN-lme4 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
An implementation of fast cluster-based permutation analysis (CPA) for
densely-sampled time data developed in Maris & Oostenveld, 2007
<doi:10.1016/j.jneumeth.2007.03.024>. Supports (generalized,
mixed-effects) regression models for the calculation of timewise
statistics. Provides both a wholesale and a piecemeal interface to the CPA
procedure with an emphasis on interpretability and diagnostics. Integrates
'Julia' libraries 'MixedModels.jl' and 'GLM.jl' for performance
improvements, with additional functionalities for interfacing with 'Julia'
from 'R' powered by the 'JuliaConnectoR' package.

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
