%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  yaap
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Archetypal Analysis Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-generics >= 0.1.3
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-generics >= 0.1.3
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-nnls 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
Fits archetypal analysis models, including Euclidean, probabilistic,
kernel, and directional variants. Methods include classical archetypal
analysis from Cutler and Breiman (1994)
<doi:10.1080/00401706.1994.10485840>, PCHA and kernel variants from Mørup
and Hansen (2012) <doi:10.1016/j.neucom.2011.06.033>, probabilistic
archetypal analysis from Seth and Eugster (2016)
<doi:10.1007/s10994-015-5498-8>, directional archetypal analysis from
Olsen et al. (2022) <doi:10.3389/fnins.2022.911034>, AA++ initialization
from Mair and Sjölund (2023) <doi:10.48550/arXiv.2301.13748>,
coreset-style initialization from Mair and Brefeld (2019)
<https://proceedings.neurips.cc/paper_files/paper/2019/file/7f278ad602c7f47aa76d1bfc90f20263-Paper.pdf>,
and adapted AIC from Suleman (2017) <doi:10.1109/FUZZ-IEEE.2017.8015385>.
Provides initialization helpers, model selection paths, plotting methods,
'broom' methods, and a 'tidymodels' recipe step.

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
