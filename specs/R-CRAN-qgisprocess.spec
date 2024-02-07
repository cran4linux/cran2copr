%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qgisprocess
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Use 'QGIS' Processing Algorithms

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-processx >= 3.5.2
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-processx >= 3.5.2
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-withr 

%description
Provides seamless access to the 'QGIS' (<https://qgis.org/en/site/>)
processing toolbox using the standalone 'qgis_process' command-line
utility.  Both native and third-party (plugin) processing providers are
supported.  Beside referring data sources from file, also common objects
from 'sf', 'terra' and 'stars' are supported. The native processing
algorithms are documented by QGIS.org (2023)
<https://docs.qgis.org/latest/en/docs/user_manual/processing_algs/>.

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
