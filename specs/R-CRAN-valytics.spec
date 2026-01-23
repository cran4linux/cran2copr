%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  valytics
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Analytical Method Comparison and Validation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-robslopes 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-robslopes 

%description
Provides statistical methods for analytical method comparison and
validation studies. Implements Bland-Altman analysis for assessing
agreement between measurement methods (Bland & Altman (1986)
<doi:10.1016/S0140-6736(86)90837-8>), Passing-Bablok regression for
non-parametric method comparison (Passing & Bablok (1983)
<doi:10.1515/cclm.1983.21.11.709>), and Deming regression accounting for
measurement error in both variables (Linnet (1993)
<doi:10.1093/clinchem/39.3.424>). Also includes tools for setting quality
goals based on biological variation (Fraser & Petersen (1993)
<doi:10.1093/clinchem/39.7.1447>) and calculating Six Sigma metrics.
Commonly used in clinical laboratory method validation. Provides
publication-ready plots and comprehensive statistical summaries.

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
