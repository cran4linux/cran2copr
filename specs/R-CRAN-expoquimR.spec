%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  expoquimR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Qualitative and Quantitative Assessment of Occupational Chemical Exposure Risk

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides a unified toolkit for occupational chemical exposure risk
assessment, implementing three internationally recognised methods end to
end: the qualitative control-banding methods COSHH Essentials (UK Health
and Safety Executive) and the method of the French National Research and
Safety Institute (INRS), together with the quantitative statistical
procedure of the UNE-EN 689 standard for comparing measured exposure
levels against occupational exposure limits. Every step of each method,
from hazard banding and exposure scoring to lognormal or normal
distribution fitting, one-sided tolerance limits, and monitoring-interval
recommendations, is implemented as a small, independently callable, and
unit-tested function, so assessments are reproducible and auditable
without depending on any graphical interface. Optional 'shiny'
applications provide a guided, interactive workflow for occupational
hygienists and health and safety practitioners who prefer not to write
code. References: UK Health and Safety Executive (2003)
<https://www.hse.gov.uk/coshh/essentials/index.htm>; Mallet, Pilorget and
Berne (2013, ISBN:978-2-7389-2166-2) "Evaluation du risque chimique" INRS
ED 6084; European Committee for Standardisation (2018)
<https://www.en-standard.eu/bs-en-689-2018-workplace-exposure-measurement-of-exposure-by-inhalation-to-chemical-agents-strategy-for-testing-compliance-with-occupational-exposure-limit-values/>.

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
