%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gasanalyzer
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Import, Recompute and Analyze Data from Portable Gas Analyzers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyxl >= 1.0.8
BuildRequires:    R-CRAN-jsonify 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-tidyxl >= 1.0.8
Requires:         R-CRAN-jsonify 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-CRAN-units 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-xml2 

%description
The gasanalyzer R package offers methods for importing, preprocessing, and
analyzing data related to photosynthetic characteristics (gas exchange,
chlorophyll fluorescence and isotope ratios). It translates variable names
into a standard format, and can recalculate derived, physiological
quantities using imported or predefined equations. The package also allows
users to assess the sensitivity of their results to different assumptions
used in the calculations. See also Tholen (2024)
<doi:10.1093/aobpla/plae035>.

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
