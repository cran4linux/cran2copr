%global packname  officer
%global packver   0.3.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.14
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulation of Microsoft Word and PowerPoint Documents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zip >= 2.1.0
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-zip >= 2.1.0
Requires:         R-CRAN-xml2 >= 1.1.0
Requires:         R-CRAN-R6 
Requires:         R-grDevices 
Requires:         R-CRAN-uuid 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-graphics 

%description
Access and manipulate 'Microsoft Word' and 'Microsoft PowerPoint'
documents from R. The package focuses on tabular and graphical reporting
from R; it also provides two functions that let users get document content
into data objects. A set of functions lets add and remove images, tables
and paragraphs of text in new or existing documents. When working with
'PowerPoint' presentations, slides can be added or removed; shapes inside
slides can also be added or removed. When working with 'Word' documents, a
cursor can be used to help insert or delete content at a specific location
in the document. The package does not require any installation of
Microsoft products to be able to write Microsoft files.

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
