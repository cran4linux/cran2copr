%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mschart
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Chart Generation for 'Microsoft Word' and 'Microsoft PowerPoint' Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-officer >= 0.3.6
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-utils 
Requires:         R-CRAN-xml2 >= 1.1.0
Requires:         R-CRAN-officer >= 0.3.6
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-writexl 
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 
Requires:         R-utils 

%description
Create native charts for 'Microsoft PowerPoint' and 'Microsoft Word'
documents. These can then be edited and annotated. Functions are provided
to let users create charts, modify and format their content. The chart's
underlying data is automatically saved within the 'Word' document or
'PowerPoint' presentation. It extends package 'officer' that does not
contain any feature for 'Microsoft' native charts production.

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
