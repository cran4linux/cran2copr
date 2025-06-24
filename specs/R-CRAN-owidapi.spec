%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  owidapi
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access the Our World in Data Chart API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.0.0
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-jsonlite >= 1.0.0
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Retrieve data from the Our World in Data (OWID) Chart API
<https://docs.owid.io/projects/etl/api/>. OWID provides public access to
more than 5,000 charts focusing on global problems such as poverty,
disease, hunger, climate change, war, existential risks, and inequality.

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
