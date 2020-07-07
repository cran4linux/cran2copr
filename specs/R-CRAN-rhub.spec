%global packname  rhub
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Connect to 'R-hub'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rcmdcheck >= 1.2.1
BuildRequires:    R-CRAN-cli >= 1.1.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rematch 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-whoami 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-rcmdcheck >= 1.2.1
Requires:         R-CRAN-cli >= 1.1.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rematch 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-whoami 
Requires:         R-CRAN-withr 

%description
Run 'R CMD check' on any of the 'R-hub' (<https://builder.r-hub.io/>)
architectures, from the command line. The current architectures include
'Windows', 'macOS', 'Solaris' and various 'Linux' distributions.

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
%doc %{rlibdir}/%{packname}/bin
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
