%global __brp_check_rpaths %{nil}
%global packname  UncertainInterval
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Uncertain Interval Methods for Three-Way Cut-Point Determination in Test Results

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-car 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-shiny 

%description
Functions for the determination of an uncertain interval, that is, a range
of test scores that is inconclusive and does not allow a classification
other than 'Uncertain' (Reference: J.A. Landsheer (2016)
<doi:10.1371/journal.pone.0166007>).

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
