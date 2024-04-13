%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  washdata
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Urban Water and Sanitation Survey Dataset

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Urban water and sanitation survey dataset collected by Water and
Sanitation for the Urban Poor (WSUP) with technical support from Valid
International. These citywide surveys have been collecting data allowing
water and sanitation service levels across the entire city to be
characterised, while also allowing more detailed data to be collected in
areas of the city of particular interest. These surveys are intended to
generate useful information for others working in the water and sanitation
sector. Current release version includes datasets collected from a survey
conducted in Dhaka, Bangladesh in March 2017. This survey in Dhaka is one
of a series of surveys to be conducted by WSUP in various cities in which
they operate including Accra, Ghana; Nakuru, Kenya; Antananarivo,
Madagascar; Maputo, Mozambique; and, Lusaka, Zambia. This package will be
updated once the surveys in other cities are completed and datasets have
been made available.

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
