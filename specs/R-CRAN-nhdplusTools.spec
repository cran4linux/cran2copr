%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nhdplusTools
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          NHDPlus Tools

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-hydroloom 
BuildRequires:    R-CRAN-dataRetrieval 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-maptiles 
BuildRequires:    R-CRAN-mapsf 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-hydroloom 
Requires:         R-CRAN-dataRetrieval 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-units 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-R.utils 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-maptiles 
Requires:         R-CRAN-mapsf 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-arrow 
Requires:         R-tools 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-digest 

%description
Tools for traversing and working with National Hydrography Dataset Plus
(NHDPlus) data. All methods implemented in 'nhdplusTools' are available in
the NHDPlus documentation available from the US Environmental Protection
Agency <https://www.epa.gov/waterdata/basic-information>.

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
