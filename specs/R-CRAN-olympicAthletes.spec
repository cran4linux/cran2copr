%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  olympicAthletes
%global packver   0.5.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.10
Release:          1%{?dist}%{?buildtag}
Summary:          Olympic Athlete Event Data, Athens 1896 to Milano-Cortina 2026

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch

%description
A tidy, long-format dataset of every athlete-event participation in the
modern Olympic Games, spanning Athens 1896 through Milano-Cortina 2026
(about 315,000 rows). Extends the rgriff23 'Olympic_history' dataset
(1896-2016) with five additional editions scraped from Olympedia
(<https://www.olympedia.org>): PyeongChang 2018, Tokyo 2020, Beijing 2022,
Paris 2024, and Milano-Cortina 2026. Companion datasets cover
edition-level metadata and verified medal tables for every edition from
1896 to 2026.

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
