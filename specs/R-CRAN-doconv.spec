%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doconv
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Document Conversion to 'PDF' or 'PNG'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       libreoffice
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-locatexec 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-tools 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-locatexec 
Requires:         R-CRAN-processx 
Requires:         R-tools 

%description
It provides the ability to generate images from documents of different
types. Three main features are provided: functions for generating document
thumbnails, functions for performing visual tests of documents and a
function for updating fields and table of contents of a 'Microsoft Word'
or 'RTF' document. In order to work, 'LibreOffice' must be installed on
the machine and or 'Microsoft Word'. If the latter is available, it can be
used to produce PDF documents or images identical to the originals;
otherwise, 'LibreOffice' is used and the rendering can be sometimes
different from the original documents.

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
