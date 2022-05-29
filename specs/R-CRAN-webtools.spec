%global __brp_check_rpaths %{nil}
%global packname  webtools
%global packver   0.7.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.10
Release:          1%{?dist}%{?buildtag}
Summary:          Various Useful Web Tools (Including Full CRAN Dataset Search and Fetch)

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-pkgsearch 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-pkgsearch 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 

%description
A set of useful web tools to improve your productivity. Including:
searching DuckDuckGo; finding and loading datasets across all CRAN
packages (not just those you've installed); sharing a file to a paste-bin;
getting a fast GUID.

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
