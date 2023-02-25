%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RRRR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Online Robust Reduced-Rank Regression Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Methods for estimating online robust reduced-rank regression. The Gaussian
maximum likelihood estimation method is described in Johansen, S. (1991)
<doi:10.2307/2938278>. The majorisation-minimisation estimation method is
partly described in Zhao, Z., & Palomar, D. P. (2017)
<doi:10.1109/GlobalSIP.2017.8309093>. The description of the generic
stochastic successive upper-bound minimisation method and the sample
average approximation can be found in Razaviyayn, M., Sanjabi, M., & Luo,
Z. Q. (2016) <doi:10.1007/s10107-016-1021-7>.

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
