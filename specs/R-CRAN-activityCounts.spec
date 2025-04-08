%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  activityCounts
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generate ActiLife Counts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 

%description
ActiLife software generates activity counts from data collected by
Actigraph accelerometers
<https://s3.amazonaws.com/actigraphcorp.com/wp-content/uploads/2017/11/26205758/ActiGraph-White-Paper_What-is-a-Count_.pdf>.
Actigraph is one of the most common research-grade accelerometers. There
is considerable research validating and developing algorithms for human
activity using ActiLife counts. Unfortunately, ActiLife counts are
proprietary and difficult to implement if researchers use different
accelerometer brands. The code creates ActiLife counts from raw
acceleration data for different accelerometer brands and it is developed
based on the study done by Brond and others (2017)
<doi:10.1249/MSS.0000000000001344>.

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
