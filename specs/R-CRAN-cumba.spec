%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cumba
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Carbon Use Model for Yield and Brix Assessment in Processing Tomato

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tibble 

%description
A daily time-step crop model for processing tomato that simulates thermal
time, phenology, root growth, a three-layer soil-water balance, carbon
accumulation modulated by heat, cold and water stress, and predicts
fresh-fruit yield and Brix at harvest. Two top-level entry points are
provided: cumba_experiment() replays observed irrigation schedules (used
for calibration), and cumba_scenario() runs the model in
deficit-irrigation scenario mode, with irrigation triggered automatically
when the crop water status falls below phase-specific thresholds. Methods
build on Yan and Hunt (1999) <doi:10.1006/anbo.1999.0955>, Zhao et al.
(2019) <doi:10.1016/j.eja.2019.01.009>, Casadebaig et al. (2011)
<doi:10.1016/j.agrformet.2010.09.012> and Prudent et al. (2010)
<doi:10.1093/jxb/erq318>; the field dataset used for calibration is
described in Carucci et al. (2024) <doi:10.1016/j.dib.2024.110225>.

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
