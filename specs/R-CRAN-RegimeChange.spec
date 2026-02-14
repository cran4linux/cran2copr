%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RegimeChange
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Regime Change Detection in Time Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-stats 
Requires:         R-CRAN-magrittr 

%description
A unified framework for detecting regime changes (changepoints) in time
series data. Implements both frequentist methods including Cumulative Sum
(CUSUM, Page (1954) <doi:10.1093/biomet/41.1-2.100>), Pruned Exact Linear
Time (PELT, Killick, Fearnhead, and Eckley (2012)
<doi:10.1080/01621459.2012.737745>), Binary Segmentation, and Wild Binary
Segmentation, as well as Bayesian methods such as Bayesian Online
Changepoint Detection (BOCPD, Adams and MacKay (2007)
<doi:10.48550/arXiv.0710.3742> and Shiryaev-Roberts. Supports offline
analysis for retrospective detection and online monitoring for real-time
surveillance. Provides rigorous uncertainty quantification through
confidence intervals and posterior distributions. Handles univariate and
multivariate series with detection of changes in mean, variance, trend,
and distributional properties.

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
