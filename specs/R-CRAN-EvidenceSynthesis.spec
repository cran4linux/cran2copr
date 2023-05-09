%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EvidenceSynthesis
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Synthesizing Causal Evidence in a Distributed Research Network

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Cyclops >= 3.1.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-EmpiricalCalibration 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-BeastJar 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
Requires:         R-CRAN-Cyclops >= 3.1.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-EmpiricalCalibration 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-BeastJar 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rlang 
Requires:         R-methods 

%description
Routines for combining causal effect estimates and study diagnostics
across multiple data sites in a distributed study, without sharing
patient-level data. Allows for normal and non-normal approximations of the
data-site likelihood of the effect parameter.

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
