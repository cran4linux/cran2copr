%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PupilPre
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Preprocessing Pupil Size Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-zoo >= 1.8.4
BuildRequires:    R-CRAN-mgcv >= 1.8.16
BuildRequires:    R-CRAN-VWPre >= 1.2.0
BuildRequires:    R-CRAN-robustbase >= 0.93.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-signal >= 0.7.6
BuildRequires:    R-CRAN-tidyr >= 0.6.0
BuildRequires:    R-CRAN-shiny >= 0.14.2
BuildRequires:    R-CRAN-rlang >= 0.1.1
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-zoo >= 1.8.4
Requires:         R-CRAN-mgcv >= 1.8.16
Requires:         R-CRAN-VWPre >= 1.2.0
Requires:         R-CRAN-robustbase >= 0.93.3
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-signal >= 0.7.6
Requires:         R-CRAN-tidyr >= 0.6.0
Requires:         R-CRAN-shiny >= 0.14.2
Requires:         R-CRAN-rlang >= 0.1.1

%description
Pupillometric data collected using SR Research Eyelink eye trackers
requires significant preprocessing. This package contains functions for
preparing pupil dilation data for visualization and statistical analysis.
Specifically, it provides a pipeline of functions which aid in data
validation, the removal of blinks/artifacts, downsampling, and baselining,
among others. Additionally, plotting functions for creating grand average
and conditional average plots are provided. See the vignette for samples
of the functionality. The package is designed for handling data collected
with SR Research Eyelink eye trackers using Sample Reports created in SR
Research Data Viewer.

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
