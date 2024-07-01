%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mevr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting the Metastatistical Extreme Value Distribution MEVD

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-bamlss 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-EnvStats 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-bamlss 
Requires:         R-CRAN-mgcv 

%description
Extreme value analysis with the metastatistical extreme value distribution
MEVD (Marani and Ignaccolo, 2015, <doi:10.1016/j.advwatres.2015.03.001>)
and some of its variants. In particular, analysis can be performed with
the simplified metastatistical extreme value distribution SMEV (Marra et
al., 2019, <doi:10.1016/j.advwatres.2019.04.002>) and the temporal
metastatistical extreme value distribution TMEV (Falkensteiner et al.,
2023, <doi:10.1016/j.wace.2023.100601>). Parameters can be estimated with
probability weighted moments, maximum likelihood and least squares. The
data can also be left-censored prior to a fit. Density, distribution
function, quantile function and random generation for the MEVD, SMEV and
TMEV are included. In addition, functions for the calculation of return
levels including confidence intervals are provided. For a description of
use cases please see the provided references.

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
