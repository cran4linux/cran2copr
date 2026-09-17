%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MFT
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Multiple Filter Test for Change Point Detection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides statistical tests and algorithms for the detection of change
points in time series and point processes - particularly for changes in
the mean in time series and for changes in the rate and in the variance in
point processes. References - Michael Messer, Marietta Kirchner, Julia
Schiemann, Jochen Roeper, Ralph Neininger and Gaby Schneider (2014), A
multiple filter test for the detection of rate changes in renewal
processes with varying variance <doi:10.1214/14-AOAS782>. Stefan Albert,
Michael Messer, Julia Schiemann, Jochen Roeper, Gaby Schneider (2017),
Multi-scale detection of variance changes in renewal processes in the
presence of rate change points <doi:10.1111/jtsa.12254>. Michael Messer,
Kaue M. Costa, Jochen Roeper and Gaby Schneider (2017), Multi-scale
detection of rate changes in spike trains with weak dependencies
<doi:10.1007/s10827-016-0635-3>. Michael Messer, Stefan Albert and Gaby
Schneider (2018), The multiple filter test for change point detection in
time series <doi:10.1007/s00184-018-0672-1>. Michael Messer, Hendrik
Backhaus, Albrecht Stroh and Gaby Schneider (2020) A multi-scale approach
for testing and detecting peaks in time series
<doi:10.1080/02331888.2020.1823980>.

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
