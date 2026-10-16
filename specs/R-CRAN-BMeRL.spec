%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BMeRL
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Median Residual Life Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Nonparametric estimation of the bivariate median residual life function of
Kayid et al. (2020) for complete and right-censored paired lifetimes.
Order-restricted estimation for two groups is also provided, following
Khan and Ghebremichael (2026). For censored data the bivariate survival
function is estimated by the method of Lin and Ying (1993). Simultaneous
confidence intervals are obtained by the percentile bootstrap approach of
Mandel and Betensky (2008), and the estimated functions can be drawn as
surface plots. See the accompanying vignette 'BMeRL' for a detailed
introduction. Kayid, M., Shafaei Noughabi, M., and Abouammoh, A. M. (2020)
<doi:10.1007/s00357-018-9300-z>; Khan, R. A., and Ghebremichael, M. (2026)
<doi:10.1002/bimj.70112>; Lin, D. Y., and Ying, Z. (1993)
<doi:10.1093/biomet/80.3.573>; Mandel, M., and Betensky, R. A. (2008)
<doi:10.1016/j.csda.2007.07.005>.

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
