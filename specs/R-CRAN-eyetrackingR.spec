%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eyetrackingR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Eye-Tracking Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0
BuildRequires:    R-CRAN-zoo >= 1.7.12
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-broom >= 0.3.7
BuildRequires:    R-CRAN-tidyr >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 2.0
Requires:         R-CRAN-zoo >= 1.7.12
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-broom >= 0.3.7
Requires:         R-CRAN-tidyr >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-lazyeval >= 0.1.10
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-rlang 

%description
Addresses tasks along the pipeline from raw data to analysis and
visualization for eye-tracking data. Offers several popular types of
analyses, including linear and growth curve time analyses,
onset-contingent reaction time analyses, as well as several non-parametric
bootstrapping approaches. For references to the approach see Mirman, Dixon
& Magnuson (2008) <doi:10.1016/j.jml.2007.11.006>, and Barr (2008)
<doi:10.1016/j.jml.2007.09.002>.

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
