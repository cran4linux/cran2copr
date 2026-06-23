%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NeutroSplitStripAnalysis
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Neutrosophic Analysis of Split-Plot and Strip-Plot Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Provides methods for Neutrosophic Analysis of Variance (NANOVA) for
split-plot and strip-plot experimental designs using interval-valued
observations. The package computes neutrosophic sums of squares, mean
squares, interval-valued F-statistics, significance tests, and Least
Significant Difference (LSD) based multiple comparisons for main plot, sub
plot, horizontal factor, vertical factor, and interaction effects. For
crisp data, users may provide identical lower and upper response values to
obtain results equivalent to classical analysis of variance. The basic
idea of neutrosophic statistics is obtained from Smarandache (2014)
<https://fs.unm.edu/NeutrosophicStatistics.pdf>, while the analysis
procedures implemented in this package are newly developed.

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
