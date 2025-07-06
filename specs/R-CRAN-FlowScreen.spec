%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FlowScreen
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Daily Streamflow Trend and Change Point Screening

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zyp 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-evir 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-zyp 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-evir 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 

%description
Screens daily streamflow time series for temporal trends and
change-points. This package has been primarily developed for assessing the
quality of daily streamflow time series. It also contains tools for
plotting and calculating many different streamflow metrics. The package
can be used to produce summary screening plots showing change-points and
significant temporal trends for high flow, low flow, and/or baseflow
statistics, or it can be used to perform more detailed hydrological time
series analyses. The package was designed for screening daily streamflow
time series from Water Survey Canada and the United States Geological
Survey but will also work with streamflow time series from many other
agencies. Package update to version 2.0 made updates to read.flows
function to allow loading of GRDC and ROBIN streamflow record formats.
This package uses the `changepoint` package for change point detection.
For more information on change point methods, see the changepoint package
at <https://cran.r-project.org/package=changepoint>.

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
