%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CepalStatR
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access to the 'CEPALSTAT API'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-collapsibleTree 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-collapsibleTree 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-htmlwidgets 

%description
Explore metadata and retrieve indicators from the statistical portal of
the Economic Commission for Latin America and the Caribbean
<https://statistics.cepal.org/portal/cepalstat/>. Provides a reproducible
interface to access the 'CEPALSTAT API', organize data into tidy formats,
and generate both static and interactive visualizations.

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
