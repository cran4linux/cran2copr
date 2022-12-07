%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contentid
%global packver   0.0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.16
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface for Content-Based Identifiers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openssl >= 1.4.2
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-tools 
BuildRequires:    R-methods 
Requires:         R-CRAN-openssl >= 1.4.2
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fs 
Requires:         R-tools 
Requires:         R-methods 

%description
An interface for creating, registering, and resolving content-based
identifiers for data management. Content-based identifiers rely on the
'cryptographic' hashes to refer to the files they identify, thus, anyone
possessing the file can compute the identifier using a well-known standard
algorithm, such as 'SHA256'.  By registering a URL at which the content is
accessible to a public archive (such as Hash Archive) or depositing data
in a scientific repository such 'Zenodo', 'DataONE' or 'SoftwareHeritage',
the content identifier can serve many functions typically associated with
A Digital Object Identifier ('DOI').  Unlike location-based identifiers
like 'DOIs', content-based identifiers permit the same content to be
registered in many locations.

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
