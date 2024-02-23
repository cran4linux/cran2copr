%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mppR
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Parent Population QTL Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-qtl 
Requires:         R-stats 
Requires:         R-utils 

%description
Analysis of experimental multi-parent populations to detect regions of the
genome (called quantitative trait loci, QTLs) influencing phenotypic
traits measured in unique and multiple environments. The population must
be composed of crosses between a set of at least three parents (e.g.
factorial design, 'diallel', or nested association mapping). The functions
cover data processing, QTL detection, and results visualization. The
implemented methodology is described in Garin, Wimmer, Mezmouk, Malosetti
and van Eeuwijk (2017) <doi:10.1007/s00122-017-2923-3>, in Garin,
Malosetti and van Eeuwijk (2020) <doi: 10.1007/s00122-020-03621-0>, and in
Garin, Diallo, Tekete, Thera, ..., and Rami (2024) <doi:
10.1093/genetics/iyae003>.

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
