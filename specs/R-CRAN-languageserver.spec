%global packname  languageserver
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Language Server Protocol

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-callr >= 3.0.0
BuildRequires:    R-CRAN-lintr >= 1.0.3
BuildRequires:    R-CRAN-styler >= 1.0.2
BuildRequires:    R-CRAN-collections 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-repr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr >= 3.0.0
Requires:         R-CRAN-lintr >= 1.0.3
Requires:         R-CRAN-styler >= 1.0.2
Requires:         R-CRAN-collections 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-repr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 

%description
An implementation of the Language Server Protocol for R. The Language
Server protocol is used by an editor client to integrate features like
auto completion. See
<https://microsoft.github.io/language-server-protocol> for details.

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
%doc %{rlibdir}/%{packname}/projects
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
