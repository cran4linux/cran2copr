%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BFS
%global packver   0.5.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.11
Release:          1%{?dist}%{?buildtag}
Summary:          Get Data from the Swiss Federal Statistical Office

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-pxweb 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rstac 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-pxweb 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rstac 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-fs 
Requires:         R-tools 
Requires:         R-CRAN-lifecycle 

%description
Search and download data from the Swiss Federal Statistical Office (BFS)
APIs <https://www.bfs.admin.ch/>.

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
