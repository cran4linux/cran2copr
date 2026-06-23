%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMAtools
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Data Management Tools for Real-Time Monitoring/Ecological Momentary Assessment Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sjstats >= 0.10.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-sjstats >= 0.10.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-plyr 

%description
Do data management functions common in real-time monitoring (also called:
ecological momentary assessment, experience sampling, micro-longitudinal)
data, including creating power curves for multilevel data, centering on
participant means and merging event-level data into momentary data sets
where you need the events to correspond to the nearest data point in the
momentary data. For background on this data type see Shiffman, Stone and
Hufford (2008) <doi:10.1146/annurev.clinpsy.3.022806.091415>, and on the
centering methods see Enders and Tofighi (2007)
<doi:10.1037/1082-989X.12.2.121>. This is VERY early release software, and
more features will be added over time.

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
