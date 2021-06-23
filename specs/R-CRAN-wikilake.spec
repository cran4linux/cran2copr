%global __brp_check_rpaths %{nil}
%global packname  wikilake
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scrape Lake Metadata Tables from Wikipedia

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-WikipediR 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-selectr 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-WikipediR 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-sp 
Requires:         R-graphics 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-selectr 
Requires:         R-CRAN-units 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Scrape lake metadata tables from Wikipedia <https://www.wikipedia.org/>.

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
