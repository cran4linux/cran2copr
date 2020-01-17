%global packname  biocompute
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Create and Manipulate BioCompute Objects

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-methods 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rmarkdown 

%description
Tools to create, validate, and export BioCompute Objects described in King
et al. (2019) <doi:10.17605/osf.io/h59uh>. Users can encode information in
data frames, and compose BioCompute Objects from the domains defined by
the standard. A checksum validator and a JSON schema validator are
provided. This package also supports exporting BioCompute Objects as JSON,
PDF, HTML, or 'Word' documents, and exporting to cloud-based platforms.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bco
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/schemas
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
