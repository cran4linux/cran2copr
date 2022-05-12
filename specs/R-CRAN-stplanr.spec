%global __brp_check_rpaths %{nil}
%global packname  stplanr
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sustainable Transport Planning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-geosphere >= 1.5.7
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-maptools >= 0.9.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.100.5.0
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-sf >= 0.6.3
BuildRequires:    R-CRAN-nabor >= 0.5.0
BuildRequires:    R-CRAN-rgeos >= 0.3.28
BuildRequires:    R-CRAN-rlang >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-lwgeom >= 0.1.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-geosphere >= 1.5.7
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-maptools >= 0.9.3
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-sf >= 0.6.3
Requires:         R-CRAN-nabor >= 0.5.0
Requires:         R-CRAN-rgeos >= 0.3.28
Requires:         R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-lwgeom >= 0.1.4
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pbapply 

%description
Tools for transport planning with an emphasis on spatial transport data
and non-motorized modes. Enables common transport planning tasks
including: downloading and cleaning transport datasets; creating
geographic "desire lines" from origin-destination (OD) data; route
assignment, locally and via interfaces to routing services such as
<https://cyclestreets.net/> and calculation of route segment attributes
such as bearing. The package implements the 'travel flow aggregration'
method described in Morgan and Lovelace (2020)
<doi:10.1177/2399808320942779>. Further information on the package's aim
and scope can be found in the vignettes and in a paper in the R Journal
(Lovelace and Ellison 2018) <doi:10.32614/RJ-2018-053>. This package
Suggests the 'pct' package which at the time of writing is unavailable on
CRAN. You can install it from the repository 'itsleeds/pct' on GitHub.

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
