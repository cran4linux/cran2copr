%global __brp_check_rpaths %{nil}
%global packname  flatxml
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Working with XML Files as R Dataframes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-crayon 

%description
On import, the XML information is converted to a dataframe that reflects
the hierarchical XML structure. Intuitive functions allow to navigate
within this transparent XML data structure (without any knowledge of
'XPath'). 'flatXML' also provides tools to extract data from the XML into
a flat dataframe that can be used to perform statistical operations. It
also supports converting dataframes to XML.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
