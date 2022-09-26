%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adaptsmoFMRI
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Smoothing of FMRI Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MCMCpack 
Requires:         R-parallel 

%description
Adaptive smoothing functions for estimating the blood oxygenation level
dependent (BOLD) effect by using functional Magnetic Resonance Imaging
(fMRI) data, based on adaptive Gauss Markov random fields, for real as
well as simulated data. The implemented models make use of efficient
Markov Chain Monte Carlo methods. Implemented methods are based on the
research developed by A. Brezger, L. Fahrmeir, A. Hennerfeind (2007)
<https://www.jstor.org/stable/4626770>.

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
