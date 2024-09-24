%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  esci
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation Statistics with Confidence Intervals

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jmvcore >= 0.8.5
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-sadists 
BuildRequires:    R-CRAN-statpsych 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-CRAN-jmvcore >= 0.8.5
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-sadists 
Requires:         R-CRAN-statpsych 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-mathjaxr 

%description
A collection of functions and 'jamovi' module for the estimation approach
to inferential statistics, the approach which emphasizes effect sizes,
interval estimates, and meta-analysis. Nearly all functions are based on
'statpsych' and 'metafor'.  This package is still under active
development, and breaking changes are likely, especially with the plot and
hypothesis test functions.  Data sets are included for all examples from
Cumming & Calin-Jageman (2024) <ISBN:9780367531508>.

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
