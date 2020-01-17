%global packname  rasciidoc
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Create Reports Using R and 'asciidoc'

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         asciidoc
Requires:         source-highlight
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-document 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-document 
Requires:         R-CRAN-highr 
Requires:         R-CRAN-knitr 

%description
Inspired by Karl Broman`s reader on using 'knitr' with 'asciidoc'
(<http://kbroman.org/knitr_knutshell/pages/asciidoc.html>), this is merely
a wrapper to 'knitr' and 'asciidoc'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/files
%doc %{rlibdir}/%{packname}/runit_tests
%{rlibdir}/%{packname}/INDEX
