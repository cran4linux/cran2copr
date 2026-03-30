%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rjd3bench
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Disaggregation and Benchmarking in 'JDemetra+' 3.x

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjd3toolkit >= 3.7.1
BuildRequires:    R-CRAN-rJava >= 1.0.6
BuildRequires:    R-CRAN-RProtoBuf >= 0.4.20
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rjd3toolkit >= 3.7.1
Requires:         R-CRAN-rJava >= 1.0.6
Requires:         R-CRAN-RProtoBuf >= 0.4.20
Requires:         R-stats 
Requires:         R-graphics 

%description
Interface to 'JDemetra+' 3.x (<https://github.com/jdemetra>) time series
analysis software. It provides a variety of methods for temporal
disaggregation & interpolation, benchmarking, reconciliation and
calendarization. It incorporates statistical methods described in the
latest European Statistical System (ESS) guidelines on temporal
disaggregation, benchmarking, and reconciliation (2018 edition). The
package implements highly efficient algorithms for fast and reliable
computation.

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
