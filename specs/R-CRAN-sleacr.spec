%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sleacr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Simplified Lot Quality Assurance Sampling Evaluation of Access and Coverage (SLEAC) Tools

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-stats 

%description
In the recent past, measurement of coverage has been mainly through
two-stage cluster sampled surveys either as part of a nutrition assessment
or through a specific coverage survey known as Centric Systematic Area
Sampling (CSAS). However, such methods are resource intensive and often
only used for final programme evaluation meaning results arrive too late
for programme adaptation. SLEAC, which stands for Simplified Lot Quality
Assurance Sampling Evaluation of Access and Coverage, is a low resource
method designed specifically to address this limitation and is used
regularly for monitoring, planning and importantly, timely improvement to
programme quality, both for agency and Ministry of Health (MoH) led
programmes. SLEAC is designed to complement the Semi-quantitative
Evaluation of Access and Coverage (SQUEAC) method. This package provides
functions for use in conducting a SLEAC assessment.

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
