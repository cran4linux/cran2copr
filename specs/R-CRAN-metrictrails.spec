%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metrictrails
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Processing of GNSS Streams from Sports Watches

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Tools to read, clean and standardise GNSS (Global Navigation Satellite
System) streams recorded by sports watches and similar devices, with a
focus on trail and mountain running. The pipeline reads GPX files, applies
a naming convention, sanitises coordinates (Kalman, LOESS, Gaussian kernel
or Savitzky-Golay smoothing, and red flags for implausible readings),
resamples the trajectory to a uniform spatial resolution derived from the
Nyquist criterion, and replaces elevation with values from a Digital
Elevation Model. Derived measures include speed, slope, elevation gain and
kilometre-effort, Tobler hiking function parameters fitted by quantile
regression, comparison between streams, detection of passes along a route
and map matching to a known reference trail by dynamic programming.
Methods follow Sanchez and Villena (2020) <doi:10.1177/1754337120918975>,
Sanchez et al. (2024) <doi:10.1109/ICECET61485.2024.10698606>, Sanchez et
al. (2025) <doi:10.1177/17543371251341660> and Martinez, Sanchez and Diaz
(2026) <doi:10.1109/ICECET65726.2026.11632531>.

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
