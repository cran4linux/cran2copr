%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  occUncertain
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Addressing Occurrence Point Uncertainty When Calculating Spatial Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ConR 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ConR 
Requires:         R-CRAN-rgdal 

%description
Repeatable processing of species occurrence datasets that makes it easier
to propagate georeferencing imprecisions and data input mistakes to
downstream analyses, allowing analysts to assess the impacts of these
imprecisions in quantifying range of occurrence (EOO) or area of occupancy
(AOO) . Users can use the software to: (a) change each coordinate record's
uncertainty from meters to decimal degrees, The formula for converting
from meters to decimal degrees is in part based on information from the
ESRI ArcUser magazine "Measuring in Arc-Seconds" at this
site<https://www.esri.com/news/arcuser/0400/wdside.html> (b) deal with
records that don't have uncertainty values in multiple ways, (c) create a
new random location for each occurrence using a uniform distribution with
a defined interval within the occurrence location uncertainty, and (d) use
repetitions to quantify EOO and AOO with attribute uncertainty.

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
