%global __brp_check_rpaths %{nil}
%global packname  distcomp
%global packver   1.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computations over Distributed Data without Aggregation

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-R6 >= 2.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-homomorpheR 
BuildRequires:    R-CRAN-gmp 
Requires:         R-CRAN-R6 >= 2.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-homomorpheR 
Requires:         R-CRAN-gmp 

%description
Implementing algorithms and fitting models when sites (possibly remote)
share computation summaries rather than actual data over HTTP with a
master R process (using 'opencpu', for example). A stratified Cox model
and a singular value decomposition are provided. The former makes direct
use of code from the R 'survival' package. (That is, the underlying Cox
model code is derived from that in the R 'survival' package.) Sites may
provide data via several means: CSV files, Redcap API, etc. An extensible
design allows for new methods to be added in the future and includes
facilities for local prototyping and testing. Web applications are
provided (via 'shiny') for the implemented methods to help in designing
and deploying the computations.

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
