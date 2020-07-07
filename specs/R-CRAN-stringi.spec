%global packname  stringi
%global packver   1.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          3%{?dist}
Summary:          Character String Processing Facilities

License:          file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libicu-devel >= 52
Requires:         libicu
BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 

%description
Fast, correct, consistent, portable and convenient character string/text
processing in every locale and any native encoding. Owing to the use of
the 'ICU' (International Components for Unicode) library, the package
provides 'R' users with platform-independent functions known to 'Java',
'Perl', 'Python', 'PHP' and 'Ruby' programmers. Available features
include: pattern searching (e.g., with 'Java'-like regular expressions or
the 'Unicode' collation algorithm), random string generation, case
mapping, string transliteration, concatenation, Unicode normalization,
date-time formatting and parsing and many more.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/include
