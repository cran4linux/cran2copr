%global packname  provGraphR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Creates Adjacency Matrices for Lineage Searches

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-provParseR >= 0.2
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-provParseR >= 0.2
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Creates and manages a provenance graph corresponding to the provenance
created by the 'rdtLite' package, which collects provenance from R
scripts.  'rdtLite' is available on CRAN. The provenance format is an
extension of the W3C PROV JSON format
(<https://www.w3.org/Submission/2013/SUBM-prov-json-20130424/>). The
extended JSON provenance format is described in
<https://github.com/End-to-end-provenance/ExtendedProvJson>.

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
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/testscripts
%{rlibdir}/%{packname}/INDEX
