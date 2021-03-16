%global packname  dccmidas
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          DCC Models with GARCH-MIDAS Specifications in the Univariate Step

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-utils >= 4.0.2
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-rugarch >= 1.4.4
BuildRequires:    R-CRAN-maxLik >= 1.3.8
BuildRequires:    R-CRAN-roll >= 1.1.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-Rdpack >= 1.0.0
BuildRequires:    R-CRAN-xts >= 0.12.0
BuildRequires:    R-CRAN-tseries >= 0.10.47
BuildRequires:    R-CRAN-rumidas >= 0.1.1
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats >= 4.0.2
Requires:         R-utils >= 4.0.2
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-rugarch >= 1.4.4
Requires:         R-CRAN-maxLik >= 1.3.8
Requires:         R-CRAN-roll >= 1.1.4
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-Rdpack >= 1.0.0
Requires:         R-CRAN-xts >= 0.12.0
Requires:         R-CRAN-tseries >= 0.10.47
Requires:         R-CRAN-rumidas >= 0.1.1

%description
Estimates a variety of Dynamic Conditional Correlation (DCC) models. More
in detail, the 'dccmidas' package allows the estimation of the corrected
DCC (cDCC) of Aielli (2013) <doi:10.1080/07350015.2013.771027>, the
DCC-MIDAS of Colacito et al. (2011) <doi:10.1016/j.jeconom.2011.02.013>,
the Asymmetric DCC of Cappiello et al. <doi:10.1093/jjfinec/nbl005>, and
the Dynamic Equicorrelation (DECO) of Engle and Kelly (2012)
<doi:10.1080/07350015.2011.652048>. 'dccmidas' offers the possibility of
including standard GARCH <doi:10.1016/0304-4076(86)90063-1>, GARCH-MIDAS
<doi:10.1162/REST_a_00300> and Double Asymmetric GARCH-MIDAS
<doi:10.1016/j.econmod.2018.07.025> models in the univariate estimation.
Finally, the package calculates also the var-cov matrix under two
non-parametric models: the Moving Covariance and the RiskMetrics
specifications.

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
