%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jsplyr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulate 'JSON' Data in the Browser with a 'dplyr' Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 

%description
A 'dplyr' backend for 'shiny' applications that manipulates 'JSON' data in
the web browser instead of on the server. Data manipulation verbs such as
filter, select, mutate, summarise, arrange, and joins are evaluated lazily
and translated into 'JavaScript' operations that run client-side,
following the lazy evaluation approach of 'dbplyr' but generating
'JavaScript' rather than 'SQL'. Results are returned to R asynchronously
as promises. This keeps data wrangling responsive for large data frames by
offloading the work to the client.

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
