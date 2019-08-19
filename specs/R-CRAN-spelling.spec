%global packname  spelling
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Tools for Spell Checking in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hunspell >= 3.0
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-hunspell >= 3.0
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-knitr 

%description
Spell checking common document formats including latex, markdown, manual
pages, and description files. Includes utilities to automate checking of
documentation and vignettes as a unit test during 'R CMD check'. Both
British and American English are supported out of the box and other
languages can be added. In addition, packages may define a 'wordlist' to
allow custom terminology without having to abuse punctuation.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
