%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bewrs
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Early-Warning Risk Surveillance for Healthcare Performance Monitoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 

%description
Provides Bayesian early-warning surveillance methods for monitoring
healthcare performance and patient safety outcomes. The package draws on
risk-adjusted monitoring frameworks developed by Steiner et al. (2000)
<doi:10.1093/biostatistics/1.4.441>, Spiegelhalter et al. (2003)
<doi:10.1002/sim.1546>, Cook et al. (2011)
<doi:10.1136/bmjqs.2008.031831>, and Neuburger et al. (2017)
<doi:10.1136/bmjqs-2016-005511>. The package implements Bayesian
predictive modelling, risk-adjusted monitoring, early-warning signal
detection, and graphical tools for continuous quality improvement and
healthcare performance assessment.

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
