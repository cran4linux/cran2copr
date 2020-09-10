%global packname  stringi
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Character String Processing Facilities

License:          file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libicu-devel >= 52
BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 

%description
A multitude of character string/text/natural language processing tools:
pattern searching (e.g., with 'Java'-like regular expressions or the
'Unicode' collation algorithm), random string generation, case mapping,
string transliteration, concatenation, sorting, padding, wrapping, Unicode
normalisation, date-time formatting and parsing, and many more. They are
fast, consistent, convenient, and - owing to the use of the 'ICU'
(International Components for Unicode) library - portable across all
locales and platforms.

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
