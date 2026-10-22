%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oes
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Effect-Size-Based Y-Axis Ranges

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-rstatix >= 0.7.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-rstatix >= 0.7.2
Requires:         R-stats 
Requires:         R-utils 

%description
Calculates effect-size-informed y-axis recommendations for visualizations
of independent, repeated-measures, and mixed designs. Summarizes selected
error bars, estimates conditional standardized contrasts, and generalizes
range-expansion rules using constants from single-factor, two-level
studies of Cohen's d. Recommendations beyond that studied setting have not
been empirically validated. Provides numerical results and 'ggplot2'
visualizations, including summary plots and preservation of supplied plot
layouts. Confidence-interval adjustment options follow the distinctions in
Cousineau (2017) <doi:10.5709/acp-0214-z>, including difference adjustment
and combined repeated-measures adjustment. Within-subject base intervals
use the normalization of Cousineau (2005) <doi:10.20982/tqmp.01.1.p042>
with the bias correction of Morey (2008) <doi:10.20982/tqmp.04.2.p061>.
Correlation-only intervals and intervals with both adjustments are
separate options. These references support confidence-interval
construction, not the range-expansion calibration.

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
