%global __brp_check_rpaths %{nil}
%global packname  ACV
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Out-of-Sample Forecast Evaluation and Testing under Stationarity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 

%description
Package 'ACV' (short for Affine Cross-Validation) offers an improved
time-series cross-validation loss estimator which utilizes both in-sample
and out-of-sample forecasting performance via a carefully constructed
affine weighting scheme. Under the assumption of stationarity, the
estimator is the best linear unbiased estimator of the out-of-sample loss.
Besides that, the package also offers improved versions of Diebold-Mariano
and Ibragimov-Muller tests of equal predictive ability which deliver more
power relative to their conventional counterparts. For more information,
see the accompanying article Stanek (2021) <doi:10.2139/ssrn.3996166>.

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
