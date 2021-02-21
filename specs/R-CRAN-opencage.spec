%global packname  opencage
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Geocode with the OpenCage API

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-progress >= 1.1.2
BuildRequires:    R-CRAN-memoise >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-crul >= 0.5.2
BuildRequires:    R-CRAN-ratelimitr >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-withr >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-progress >= 1.1.2
Requires:         R-CRAN-memoise >= 1.1.0
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-crul >= 0.5.2
Requires:         R-CRAN-ratelimitr >= 0.4.0
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 

%description
Geocode with the OpenCage API, either from place name to longitude and
latitude (forward geocoding) or from longitude and latitude to the name
and address of a location (reverse geocoding), see
<https://opencagedata.com/>.

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
