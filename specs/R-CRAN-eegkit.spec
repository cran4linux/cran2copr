%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eegkit
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for Electroencephalography Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-eegkitdata 
BuildRequires:    R-CRAN-bigsplines 
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-signal 
Requires:         R-CRAN-eegkitdata 
Requires:         R-CRAN-bigsplines 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-signal 

%description
Analysis and visualization tools for electroencephalography (EEG) data.
Includes functions for (i) plotting EEG data, (ii) filtering EEG data,
(iii) smoothing EEG data; (iv) frequency domain (Fourier) analysis of EEG
data, (v) Independent Component Analysis of EEG data, and (vi) simulating
event-related potential EEG data.

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
