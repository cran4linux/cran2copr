%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  alkahest
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pre-Processing XY Data from Experimental Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
A lightweight, dependency-free toolbox for pre-processing XY data from
experimental methods (i.e. any signal that can be measured along a
continuous variable). This package provides methods for baseline
estimation and correction, smoothing, normalization, integration and peaks
detection. Baseline correction methods includes polynomial fitting as
described in Lieber and Mahadevan-Jansen (2003)
<doi:10.1366/000370203322554518>, Rolling Ball algorithm after Kneen and
Annegarn (1996) <doi:10.1016/0168-583X(95)00908-6>, SNIP algorithm after
Ryan et al. (1988) <doi:10.1016/0168-583X(88)90063-8>, 4S Peak Filling
after Liland (2015) <doi:10.1016/j.mex.2015.02.009> and more.

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
