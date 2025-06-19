%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dpcR
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Digital PCR Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-chipPCR 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-dgof 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-qpcR 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rateratio.test 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-methods 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-chipPCR 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-dgof 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-qpcR 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rateratio.test 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.geom 

%description
Analysis, visualisation and simulation of digital polymerase chain
reaction (dPCR) (Burdukiewicz et al. (2016)
<doi:10.1016/j.bdq.2016.06.004>). Supports data formats of commercial
systems (Bio-Rad QX100 and QX200; Fluidigm BioMark) and other systems.

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
