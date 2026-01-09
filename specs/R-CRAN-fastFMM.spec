%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastFMM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Functional Mixed Models using Fast Univariate Inference

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-cAIC4 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lsei 
BuildRequires:    R-CRAN-refund 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-lmeresampler 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lme4 
Requires:         R-parallel 
Requires:         R-CRAN-cAIC4 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lsei 
Requires:         R-CRAN-refund 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-lmeresampler 
Requires:         R-stats 
Requires:         R-methods 

%description
Implementation of the fast univariate inference approach (Cui et al.
(2022) <doi:10.1080/10618600.2021.1950006>, Loewinger et al. (2024)
<doi:10.7554/eLife.95802.2>, Xin et al. (2025)) for fitting functional
mixed models. User guides and Python package information can be found at
<https://github.com/gloewing/photometry_FLMM>.

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
