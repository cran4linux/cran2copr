%global packname  BioInstaller
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          3%{?dist}%{?buildtag}
Summary:          Integrator of Bioinformatics Resources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.5.0
BuildRequires:    R-CRAN-RCurl >= 1.95.4.8
BuildRequires:    R-CRAN-futile.logger >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-devtools >= 1.13.2
BuildRequires:    R-CRAN-stringi >= 1.1.5
BuildRequires:    R-CRAN-configr >= 0.3.3
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-git2r >= 0.0.3
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-liteq 
Requires:         R-CRAN-R.utils >= 2.5.0
Requires:         R-CRAN-RCurl >= 1.95.4.8
Requires:         R-CRAN-futile.logger >= 1.4.1
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-devtools >= 1.13.2
Requires:         R-CRAN-stringi >= 1.1.5
Requires:         R-CRAN-configr >= 0.3.3
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-git2r >= 0.0.3
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-liteq 

%description
Can be used to integrate massive bioinformatics resources, such as
tool/script and database. It provides the R functions and Shiny web
application. Hundreds of bioinformatics tool/script and database have been
included.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
