%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contentvalidR
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Substantive and Content Validity Pretesting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides quantitative tools for substantive and content-oriented scale
pretesting. Implements item-sort indices from Anderson and Gerbing (1991)
<doi:10.1037/0021-9010.76.5.732>, exact item-sort inference following
Howard and Melloy (2016) <doi:10.1007/s10869-015-9404-y>, empirical
interpretation benchmarks from Colquitt et al. (2019)
<doi:10.1037/apl0000406>, and the construct-rating procedure of Hinkin and
Tracey (1999) <doi:10.1177/109442819922004> with HTC/HTD indices and
repeated-measures item screening. The expert-panel workflow combines
Aiken's V with score confidence intervals, Lawshe content validity ratios
with exact inference, content validity indices with modified kappa and
score intervals, item-objective congruence, and panel-level agreement
using Krippendorff's alpha as described by Hayes and Krippendorff (2007)
<doi:10.1080/19312450709336664>. Also provides judge and rater
heterogeneity analysis following the generalizability-theory treatment of
content-validity ratings in Crocker, Llabre and Miller (1988)
<doi:10.1111/j.1745-3984.1988.tb00309.x>, content-domain coverage and
expert-perceived content structure following Sireci and Geisinger (1992)
<doi:10.1177/014662169201600102>, comparison across successive pretest
rounds, and exact expert-panel planning. Where published methods compete,
users choose among them through arguments with evidence-based defaults.
User-facing workflows emphasize interpretable summaries and transparent
review recommendations rather than isolated coefficients.

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
