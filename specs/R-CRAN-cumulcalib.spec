%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cumulcalib
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cumulative Calibration Assessment for Prediction Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Tools for visualization of, and inference on, the calibration of
prediction models on the cumulative domain. This provides a method for
evaluating calibration of risk prediction models without having to group
the data or use tuning parameters (e.g., loess bandwidth). This package
implements the methodology described in Sadatsafavi and Petkau (2024)
<doi:10.1002/sim.10138>. The core of the package is cumulcalib(), which
takes in vectors of binary responses and predicted risks. The package also
implements non-parametric assessment of the calibration of individualized
treatment effect (ITE) models using data from a randomized trial, via
cumulcalibITE(), as described in Sadatsafavi et al. (2025)
<doi:10.48550/arXiv.2512.08140>. The plot() and summary() methods are
implemented for the results returned by cumulcalib() and cumulcalibITE().

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
