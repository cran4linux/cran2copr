%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MALDIquantForeign
%global packver   0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14
Release:          1%{?dist}%{?buildtag}
Summary:          Import/Export Routines for 'MALDIquant'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-readMzXmlData >= 2.7
BuildRequires:    R-CRAN-readBrukerFlexData >= 1.7
BuildRequires:    R-CRAN-MALDIquant >= 1.16.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-readMzXmlData >= 2.7
Requires:         R-CRAN-readBrukerFlexData >= 1.7
Requires:         R-CRAN-MALDIquant >= 1.16.4
Requires:         R-methods 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-XML 

%description
Functions for reading (tab, csv, Bruker fid, Ciphergen XML, mzXML, mzML,
imzML, Analyze 7.5, CDF, mMass MSD) and writing (tab, csv, mMass MSD,
mzML, imzML) different file formats of mass spectrometry data into/from
'MALDIquant' objects.

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
