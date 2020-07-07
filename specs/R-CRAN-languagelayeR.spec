%global packname  languagelayeR
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          3%{?dist}
Summary:          Access the 'languagelayer' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-curl 
Requires:         R-utils 

%description
Improve your text analysis with languagelayer <https://languagelayer.com>,
a powerful language detection API.

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
%doc %{rlibdir}/%{packname}/articles
%doc %{rlibdir}/%{packname}/authors.html
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/index.html
%doc %{rlibdir}/%{packname}/jquery.sticky-kit.min.js
%doc %{rlibdir}/%{packname}/link.svg
%doc %{rlibdir}/%{packname}/news
%doc %{rlibdir}/%{packname}/pkgdown.css
%doc %{rlibdir}/%{packname}/pkgdown.js
%doc %{rlibdir}/%{packname}/reference
%{rlibdir}/%{packname}/INDEX
