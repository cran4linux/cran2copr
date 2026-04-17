%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hlmLab
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Linear Modeling with Visualization and Decomposition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Provides functions for visualization and decomposition in hierarchical
linear models (HLM) for applications in education, psychology, and the
social sciences. Includes variance decomposition for two-level and
three-level data structures following Snijders and Bosker (2012,
ISBN:9781849202015), intraclass correlation (ICC) estimation and design
effect computation as described in Shrout and Fleiss (1979)
<doi:10.1037/0033-2909.86.2.420>, and contextual effect decomposition via
the Mundlak (1978) <doi:10.2307/1913646> specification distinguishing
within- and between-cluster components. Supports visualization of random
slopes and cross-level interactions following Hofmann and Gavin (1998)
<doi:10.1177/014920639802400504> and Hamaker and Muthen (2020)
<doi:10.1037/met0000239>. Multilevel models are estimated using 'lme4'
(Bates et al., 2015 <doi:10.18637/jss.v067.i01>). An optional 'Shiny'
application enables interactive exploration of model components and
parameter variation. The implementation follows the multilevel modeling
framework of Raudenbush and Bryk (2002, ISBN:9780761919049).

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
