%global packname  biolink
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}
Summary:          Create Hyperlinks to Biological Databases and Resources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rentrez 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-rentrez 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-memoise 

%description
Generate urls and hyperlinks to commonly used biological databases and
resources based on standard identifiers. This is primarily useful when
writing dynamic reports that reference things like gene symbols in text or
tables, allowing you to, for example, convert gene identifiers to
hyperlinks pointing to their entry in the NCBI Gene database. Currently
supports NCBI Gene, PubMed, Gene Ontology, CRAN and Bioconductor.

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
%{rlibdir}/%{packname}/INDEX
