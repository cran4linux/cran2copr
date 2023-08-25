%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcarbon
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calibration and Analysis of Radiocarbon Dates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.model 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.linnet 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.model 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.linnet 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-knitr 

%description
Enables the calibration and analysis of radiocarbon dates, often but not
exclusively for the purposes of archaeological research. It includes
functions not only for basic calibration, uncalibration, and plotting of
one or more dates, but also a statistical framework for building
demographic and related longitudinal inferences from aggregate radiocarbon
date lists, including: Monte-Carlo simulation test (Timpson et al 2014
<doi:10.1016/j.jas.2014.08.011>), random mark permutation test (Crema et
al 2016 <doi:10.1371/journal.pone.0154809>) and spatial permutation tests
(Crema, Bevan, and Shennan 2017 <doi:10.1016/j.jas.2017.09.007>).

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
