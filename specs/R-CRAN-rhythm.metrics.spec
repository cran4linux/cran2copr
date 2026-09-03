%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rhythm.metrics
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse and Visualise Speech Rhythm and Timing Metrics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggsci 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
Calculates and visualises speech rhythm and timing metrics. The
'rhythm.metrics' package provides a standardised workflow to compute
common metrics including Delta C, Delta V, VarcoC, VarcoV, the percentage
of vocalic intervals (%%V), and both raw and normalised Pairwise
Variability Indices (rPVI, nPVI). It includes functions for calculating
and visualising these measures to facilitate cross-linguistic and
developmental rhythm research. Delta C, Delta V, and %%V measures are based
on Ramus et al. (1999) <doi:10.1016/S0010-0277(99)00058-X>; VarcoC and
VarcoV measures are based on Dellwo (2006, ISBN: 9783631554777); and
rPVI-C and nPVI-V are based on Grabe & Low (2002)
<doi:10.1515/9783110197105.2.515>.

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
