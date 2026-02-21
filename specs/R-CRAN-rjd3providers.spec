%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rjd3providers
%global packver   3.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'JDemetra+' 3.x Time Series Analysis Software

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjd3toolkit >= 3.6.0
BuildRequires:    R-CRAN-rJava >= 1.0.6
BuildRequires:    R-CRAN-rjd3jars 
Requires:         R-CRAN-rjd3toolkit >= 3.6.0
Requires:         R-CRAN-rJava >= 1.0.6
Requires:         R-CRAN-rjd3jars 

%description
Interface to 'JDemetra+' 3.x (<https://github.com/jdemetra>) time series
analysis software. It offers full access to txt, csv, xml and spreadsheets
files which are meant to be read by 'JDemetra+' Graphical User Interface.

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
