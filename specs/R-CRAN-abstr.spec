%global __brp_check_rpaths %{nil}
%global packname  abstr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to the A/B Street Transport System Simulation Software

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.6
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-jsonlite >= 1.7.2
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-sf >= 1.0.1
BuildRequires:    R-CRAN-od >= 0.3.1
BuildRequires:    R-CRAN-lwgeom >= 0.2.5
BuildRequires:    R-methods 
Requires:         R-CRAN-tibble >= 3.0.6
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-jsonlite >= 1.7.2
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-sf >= 1.0.1
Requires:         R-CRAN-od >= 0.3.1
Requires:         R-CRAN-lwgeom >= 0.2.5
Requires:         R-methods 

%description
Provides functions to convert origin-destination data, represented as
straight 'desire lines' in the 'sf' Simple Features class system, into
JSON files that can be directly imported into A/B Street
<https://www.abstreet.org>, a free and open source tool for simulating
urban transport systems and scenarios of change
<doi:10.1007/s10109-020-00342-2>.

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
