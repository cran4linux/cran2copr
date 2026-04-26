%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mschart
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Chart Generation for 'Microsoft Word', 'Microsoft Excel' and 'Microsoft PowerPoint' Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-officer >= 0.7.4
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-xml2 >= 1.1.0
Requires:         R-CRAN-officer >= 0.7.4
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-writexl 

%description
Create native charts for 'Microsoft PowerPoint', 'Microsoft Excel' and
'Microsoft Word' documents. The resulting charts can then be edited and
annotated in the host application. It provides functions to create charts
and to modify their content and formatting. The chart's underlying data is
automatically saved within the 'Word', 'Excel' or 'PowerPoint' file. It
extends the 'officer' package, which does not provide native 'Microsoft'
chart production.

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
