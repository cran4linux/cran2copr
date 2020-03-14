%global packname  GRANBase
%global packver   2.6.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.20
Release:          1%{?dist}
Summary:          Creating Continuously Integrated Package Repositories fromManifests

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         subversion
Requires:         git
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlTable >= 1.11.0
BuildRequires:    R-CRAN-switchr >= 0.13.4
BuildRequires:    R-CRAN-GRANCore 
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sendmailR 
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-desc 
Requires:         R-CRAN-htmlTable >= 1.11.0
Requires:         R-CRAN-switchr >= 0.13.4
Requires:         R-CRAN-GRANCore 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sendmailR 
Requires:         R-CRAN-covr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-stringi 
Requires:         R-stats 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-desc 

%description
Repository based tools for department and analysis level reproducibility.
'GRANBase' allows creation of custom branched, continuous
integration-ready R repositories, including incremental testing of only
packages which have changed versions since the last repository build.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/assets
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/GRAN
%doc %{rlibdir}/%{packname}/testpkgs
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
