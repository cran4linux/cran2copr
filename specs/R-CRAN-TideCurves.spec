%global __brp_check_rpaths %{nil}
%global packname  TideCurves
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Prediction of Tides

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chron >= 2.3.56
BuildRequires:    R-CRAN-fields >= 11.6
BuildRequires:    R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-chron >= 2.3.56
Requires:         R-CRAN-fields >= 11.6
Requires:         R-CRAN-data.table >= 1.14.0

%description
Tidal analysis of evenly spaced observed time series (time step 1 to 60
min) with or without shorter gaps using the harmonic representation of
inequalities. The analysis should preferably cover an observation period
of at least 19 years. For shorter periods low frequency constituents are
not taken into account, in accordance with the Rayleigh-Criterion. The
main objective of this package is to synthesize or predict a tidal time
series.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
