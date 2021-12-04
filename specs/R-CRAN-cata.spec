%global __brp_check_rpaths %{nil}
%global packname  cata
%global packver   0.0.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.10.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Check-All-that-Apply (CATA) Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Functions for analyzing check-all-that-apply (CATA) data from consumer and
sensory tests. Cochran's Q test, McNemar's test, and Penalty-Lift analysis
provided, as described in for CATA data analysis by Meyners, Castura &
Carr (2013) <doi:10.1016/j.foodqual.2013.06.010>. Cluster analysis can be
performed using b-cluster analysis. The quality of cluster analysis
solutions can be evaluated using various measures. The methods related to
b-cluster analysis are described in a pre-print manuscript by Castura,
Meyners, Varela & Naes (2021)
<https://secure.compusense.com/research/wp-content/uploads/2021/12/Castura_bcluster_submitted_20211130.pdf>.

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
