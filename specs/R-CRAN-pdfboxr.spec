%global packname  pdfboxr
%global packver   2.0.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.19
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'PDFBox'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.9.6
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-rJava >= 0.9.6
Requires:         R-CRAN-checkmate 

%description
Interface to the 'Apache' 'PDFBox' library <https://pdfbox.apache.org/>.
'PDFBox' is an open source 'Java' tool for working with 'PDF' documents.
Currently 'pdfboxr' only implements functions to extract data from
'PDF'-files.

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
