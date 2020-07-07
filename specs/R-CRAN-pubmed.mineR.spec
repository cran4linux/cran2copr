%global packname  pubmed.mineR
%global packver   1.0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.16
Release:          3%{?dist}
Summary:          Text Mining of PubMed Abstracts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-R2HTML 
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-boot 
Requires:         R-CRAN-R2HTML 

%description
Text mining of PubMed Abstracts (text and XML) from
<http://www.ncbi.nlm.nih.gov/pubmed>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
