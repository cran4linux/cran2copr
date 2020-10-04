%global packname  pdfminer
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Read Portable Document Format (PDF) Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-jsonlite 

%description
Provides an interface to 'PDFMiner'
<https://github.com/pdfminer/pdfminer.six> a 'Python' package for
extracting information from 'PDF'-files. 'PDFMiner' has the goal to get
all information available in a 'PDF'-file, position of the characters,
font type, font size and informations about lines. Which makes it the
perfect starting point for extracting tables from 'PDF'-files. More
information can be found in the package 'README'-file.

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

%files
%{rlibdir}/%{packname}
