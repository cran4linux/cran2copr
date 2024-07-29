%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaHelper
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transforms Statistical Measures Commonly Used for Meta-Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-confintr 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-confintr 

%description
Helps calculate statistical values commonly used in meta-analysis. It
provides several methods to compute different forms of standardized mean
differences, as well as other values such as standard errors and standard
deviations. The methods used in this package are described in the
following references: Altman D G, Bland J M. (2011)
<doi:10.1136/bmj.d2090> Borenstein, M., Hedges, L.V., Higgins, J.P.T. and
Rothstein, H.R. (2009) <doi:10.1002/9780470743386.ch4> Chinn S. (2000)
<doi:10.1002/1097-0258(20001130)19:22%%3C3127::aid-sim784%%3E3.0.co;2-m>
Cochrane Handbook (2011)
<https://handbook-5-1.cochrane.org/front_page.htm> Cooper, H., Hedges, L.
V., & Valentine, J. C. (2009)
<https://psycnet.apa.org/record/2009-05060-000> Cohen, J. (1977)
<https://psycnet.apa.org/record/1987-98267-000> Ellis, P.D. (2009)
<https://www.psychometrica.de/effect_size.html> Goulet-Pelletier, J.-C., &
Cousineau, D. (2018) <doi:10.20982/tqmp.14.4.p242> Hedges, L. V. (1981)
<doi:10.2307/1164588> Hedges L. V., Olkin I. (1985)
<doi:10.1016/C2009-0-03396-0> Murad M H, Wang Z, Zhu Y, Saadi S, Chu H,
Lin L et al. (2023) <doi:10.1136/bmj-2022-073141> Mayer M (2023)
<https://search.r-project.org/CRAN/refmans/confintr/html/ci_proportion.html>
Stackoverflow (2014)
<https://stats.stackexchange.com/questions/82720/confidence-interval-around-binomial-estimate-of-0-or-1>
Stackoverflow (2018) <https://stats.stackexchange.com/q/338043>.

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
