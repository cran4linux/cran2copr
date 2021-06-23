%global __brp_check_rpaths %{nil}
%global packname  rvest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Harvest (Scrape) Web Pages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.3
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-httr >= 0.5
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-selectr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-xml2 >= 1.3
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-httr >= 0.5
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-selectr 
Requires:         R-CRAN-tibble 

%description
Wrappers around the 'xml2' and 'httr' packages to make it easy to
download, then manipulate, HTML and XML.

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
