%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statioVAR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Trend Removal for Vector Autoregressive Workflows

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Detrending multivariate time-series to approximate stationarity when
dealing with intensive longitudinal data, prior to Vector Autoregressive
(VAR) or multilevel-VAR estimation. Classical VAR assumes weak
stationarity (constant first two moments), and deterministic trends
inflate spurious autocorrelation, biasing Granger-causality and
impulse-response analyses. All functions operate on raw panel data and
write detrended columns back to the data set, but differ in the level at
which the trend is estimated. See, for instance, Wang & Maxwell (2015)
<doi:10.1037/met0000030>; Burger et al. (2022)
<doi:10.4324/9781003111238-13>; Epskamp et al. (2018)
<doi:10.1177/2167702617744325>.

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
