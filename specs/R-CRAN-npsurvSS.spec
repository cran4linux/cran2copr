%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npsurvSS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size and Power Calculation for Common Non-Parametric Tests in Survival Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
A number of statistical tests have been proposed to compare two survival
curves, including the difference in (or ratio of) t-year survival,
difference in (or ratio of) p-th percentile survival, difference in (or
ratio of) restricted mean survival time, and the weighted log-rank test.
Despite the multitude of options, the convention in survival studies is to
assume proportional hazards and to use the unweighted log-rank test for
design and analysis. This package provides sample size and power
calculation for all of the above statistical tests with allowance for
flexible accrual, censoring, and survival (eg. Weibull,
piecewise-exponential, mixture cure). It is the companion R package to the
paper by Yung and Liu (2020) <doi:10.1111/biom.13196>. Specific to the
weighted log-rank test, users may specify which approximations they wish
to use to estimate the large-sample mean and variance. The default option
has been shown to provide substantial improvement over the conventional
sample size and power equations based on Schoenfeld (1981)
<doi:10.1093/biomet/68.1.316>.

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
