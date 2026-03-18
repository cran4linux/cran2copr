%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fqardl
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fourier ARDL Methods: Quantile, Nonlinear, Multi-Threshold & Unit Root Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
Requires:         R-CRAN-quantreg >= 5.0
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 

%description
Comprehensive implementation of advanced ARDL methodologies for
cointegration analysis with structural breaks and asymmetric effects.
Includes: (1) Fourier Quantile ARDL (FQARDL) - quantile regression with
Fourier approximation for analyzing relationships across the conditional
distribution; (2) Fourier Nonlinear ARDL (FNARDL) - asymmetric
cointegration with partial sum decomposition following Shin, Yu &
Greenwood-Nimmo (2014) <doi:10.1007/978-1-4899-8008-3_9>; (3)
Multi-Threshold NARDL (MTNARDL) - multiple regime asymmetry analysis; (4)
Fourier Unit Root Tests - ADF and KPSS tests with Fourier terms following
Enders & Lee (2012) <doi:10.1016/j.econlet.2012.05.019> and Becker, Enders
& Lee (2006) <doi:10.1111/j.1467-9892.2006.00490.x>. Features automatic
lag and frequency selection, PSS bounds testing following Pesaran, Shin &
Smith (2001) <doi:10.1002/jae.616>, bootstrap cointegration tests, Wald
tests for asymmetry, dynamic multiplier computation, and publication-ready
visualizations. Ported from Stata/Python by Dr. Merwan Roudane.

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
