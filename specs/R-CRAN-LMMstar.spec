%global __brp_check_rpaths %{nil}
%global packname  LMMstar
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Repeated Measurement Models for Discrete Times

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-lava 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-lava 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-sandwich 

%description
Companion R package for the course "Statistical analysis of correlated and
repeated measurements for health science researchers" taught by the
section of Biostatistics of the University of Copenhagen. It provides
functions for computing summary statistics and obtaining graphical
displays of longitudinal data, as well as for statistical modeling and
statistical inference using linear mixed model.

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
