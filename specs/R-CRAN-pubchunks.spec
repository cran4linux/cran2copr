%global packname  pubchunks
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Fetch Sections of XML Scholarly Articles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rcrossref 
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rcrossref 

%description
Get chunks of XML scholarly articles without having to know how to work
with XML. Custom mappers for each publisher and for each article section
pull out the information you want. Works with outputs from package
'fulltext', 'xml2' package documents, and file paths to XML documents.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
