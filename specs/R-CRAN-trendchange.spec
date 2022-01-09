%global __brp_check_rpaths %{nil}
%global packname  trendchange
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Innovative Trend Analysis and Time-Series Change Point Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Innovative Trend Analysis is a graphical method to examine the trends in
time series data. Sequential Mann-Kendall test uses the intersection of
prograde and retrograde series to indicate the possible change point in
time series data. Distribution free cumulative sum charts indicate
location and significance of the change point in time series. Zekai, S.
(2011). <doi:10.1061/(ASCE)HE.1943-5584.0000556>. Grayson, R. B. et al.
(1996). Hydrological Recipes: Estimation Techniques in Australian
Hydrology. Cooperative Research Centre for Catchment Hydrology, Australia,
p. 125. Sneyers, S. (1990). On the statistical analysis of series of
observations. Technical note no 5 143, WMO No 725 415. Secretariat of the
World Meteorological Organization, Geneva, 192 pp.

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
