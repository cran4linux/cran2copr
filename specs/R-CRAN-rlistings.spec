%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rlistings
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Trial Style Data Readout Listings

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-formatters >= 0.5.5
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-formatters >= 0.5.5
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Listings are often part of the submission of clinical trial data in
regulatory settings.  We provide a framework for the specific formatting
features often used when displaying large datasets in that context.

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
