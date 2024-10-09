%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cata
%global packver   0.1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Check-All-that-Apply (CATA) Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Package contains functions for analyzing check-all-that-apply (CATA) data
from consumer and sensory tests. Cochran's Q test, McNemar's test, and
Penalty-Lift analysis are provided; for details, see Meyners, Castura &
Carr (2013) <doi:10.1016/j.foodqual.2013.06.010>. Cluster analysis can be
performed using b-cluster analysis, then evaluated using various measures;
for details, see Castura, Meyners, Varela & Næs (2022)
<doi:10.1016/j.foodqual.2022.104564>. Methods are adapted to cluster
consumers based on their product-related hedonic responses; for details,
see Castura, Meyners, Pohjanheimo, Varela & Næs (2023)
<doi:10.1111/joss.12860>.

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
