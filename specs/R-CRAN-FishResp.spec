%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FishResp
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analytical Tool for Aquatic Respirometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-rMR 
BuildRequires:    R-CRAN-respirometry 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-rMR 
Requires:         R-CRAN-respirometry 

%description
Calculates metabolic rate of fish and other aquatic organisms measured
using an intermittent-flow respirometry approach. The tool is used to run
a set of graphical QC tests of raw respirometry data, correct it for
background respiration and chamber effect, filter and extract target
values of absolute and mass-specific metabolic rate. Experimental design
should include background respiration tests and measuring of one or more
metabolic rate traits. The R package is ideally integrated with the pump
controller 'PumpResp' and the DO meter 'SensResp' (open-source hardware by
FishResp). Raw respirometry data can be also imported from 'AquaResp'
(free software), 'AutoResp' ('LoligoSystems'), 'OxyView' ('PreSens'),
'Pyro Oxygen Logger' ('PyroScience') and 'Q-box Aqua' ('QubitSystems').
More information about the R package 'FishResp'is available in the
publication by Morozov et al. (2019) <doi:10.1093/conphys/coz003>.

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
