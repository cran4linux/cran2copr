%global packname  languageserver
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          2%{?dist}
Summary:          Language Server Protocol

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-callr >= 3.0.0
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-lintr >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-fs >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.2
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-styler >= 1.2.0
BuildRequires:    R-CRAN-stringi >= 1.1.7
BuildRequires:    R-CRAN-repr >= 1.1.0
BuildRequires:    R-CRAN-xmlparsedata >= 1.0.3
BuildRequires:    R-CRAN-collections >= 0.3.0
BuildRequires:    R-parallel 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr >= 3.0.0
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-lintr >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-fs >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.2
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-styler >= 1.2.0
Requires:         R-CRAN-stringi >= 1.1.7
Requires:         R-CRAN-repr >= 1.1.0
Requires:         R-CRAN-xmlparsedata >= 1.0.3
Requires:         R-CRAN-collections >= 0.3.0
Requires:         R-parallel 
Requires:         R-tools 
Requires:         R-utils 

%description
An implementation of the Language Server Protocol for R. The Language
Server protocol is used by an editor client to integrate features like
auto completion. See
<https://microsoft.github.io/language-server-protocol> for details.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/projects
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
