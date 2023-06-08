%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WebGestaltR
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Gene Set Analysis Toolkit WebGestaltR

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-parallel >= 3.3.2
BuildRequires:    R-CRAN-foreach >= 1.4.0
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-parallel >= 3.3.2
Requires:         R-CRAN-foreach >= 1.4.0
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-apcluster 
Requires:         R-CRAN-Rcpp 

%description
The web version WebGestalt <https://www.webgestalt.org> supports 12
organisms, 354 gene identifiers and 321,251 function categories. Users can
upload the data and functional categories with their own gene identifiers.
In addition to the Over-Representation Analysis, WebGestalt also supports
Gene Set Enrichment Analysis and Network Topology Analysis. The
user-friendly output report allows interactive and efficient exploration
of enrichment results. The WebGestaltR package not only supports all above
functions but also can be integrated into other pipeline or simultaneously
analyze multiple gene lists.

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
