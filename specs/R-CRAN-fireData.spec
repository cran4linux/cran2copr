%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fireData
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Connect to 'Google Firebase'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-yaml >= 2.3.0
BuildRequires:    R-CRAN-openssl >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-yaml >= 2.3.0
Requires:         R-CRAN-openssl >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-httr >= 1.4.0

%description
Provides an interface to 'Google Firebase' services
<https://firebase.google.com/>, including 'Firebase Realtime Database',
'Cloud Firestore', 'Firebase Authentication', and 'Cloud Storage for
Firebase'. Supports interactive use and 'shiny' applications as well as
automated server-side workflows. Data frames and objects can be stored and
retrieved, users can be authenticated, and files can be managed through
the services' application programming interfaces.

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
