%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dataset
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create Data Frames that are Easier to Exchange and Reuse

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-ISOcodes 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-ISOcodes 
Requires:         R-stats 
Requires:         R-utils 

%description
The aim of the 'dataset' package is to make tidy datasets easier to
release, exchange and reuse. It organizes and formats data frame 'R'
objects into well-referenced, well-described, interoperable datasets into
release and reuse ready form. A subjective interpretation of the W3C
DataSet recommendation and the datacube model
<https://www.w3.org/TR/vocab-data-cube/>, which is also used in the global
Statistical Data and Metadata eXchange standards, the application of the
connected Dublin Core
<https://www.dublincore.org/specifications/dublin-core/dcmi-terms/> and
DataCite <https://support.datacite.org/docs/datacite-metadata-schema-44/>
standards preferred by European open science repositories to improve the
findability, accessibility, interoperability and reusability of the
datasets.

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
