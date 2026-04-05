%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  misc
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions for Data and Geospatial Work

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-here 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-zip 

%description
Helpers for common data analysis tasks including missing-value summaries
and filters, simple reporting and plotting utilities, 'Excel' import and
export workflows, and reading geospatial formats (for example shapefiles
in zip archives, file geodatabases, KMZ, and KML) via 'sf' and related
packages. Also includes small project utilities such as creating
directories, gitignore scaffolding, combined package loading, and optional
'lintr' setup.

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
