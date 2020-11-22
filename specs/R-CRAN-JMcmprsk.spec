%global packname  JMcmprsk
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Models for Longitudinal and Competing Risks Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 

%description
Fit joint models of continuous or ordinal longitudinal data and
time-to-event data with competing risks. For a detailed information, see
Robert Elashoff, Gang Li and Ning Li (2016, ISBN:9781439807828); Robert M.
Elashoff,Gang Li and Ning Li (2008) <doi:10.1111/j.1541-0420.2007.00952.x>
; Ning Li, Robert Elashoff, Gang Li and Jeffrey Saver (2010)
<doi:10.1002/sim.3798> .

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
