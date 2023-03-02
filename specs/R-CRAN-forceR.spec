%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forceR
%global packver   1.0.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.20
Release:          1%{?dist}%{?buildtag}
Summary:          Force Measurement Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-filesstrings 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-roll 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-filesstrings 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-roll 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
For cleaning and analysis of graphs, such as animal closing force
measurements. 'forceR' was initially written and optimized to deal with
insect bite force measurements, but can be used for any time series.
Includes a full workflow to load, plot and crop data, correct amplifier
and baseline drifts, identify individual peak shapes (bites), rescale
(normalize) peak curves, and find best polynomial fits to describe and
analyze force curve shapes.

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
