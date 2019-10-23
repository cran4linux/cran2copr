%global packname  TCGAretriever
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Retrieve Genomic and Clinical Data from TCGA

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-graphics 

%description
The Cancer Genome Atlas (TCGA) is a program aimed at improving our
understanding of Cancer Biology. Several TCGA Datasets are available
online. 'TCGAretriever' helps accessing and downloading TCGA data hosted
on 'cBioPortal' via its Web Interface (see
<http://www.cbioportal.org/web_api.jsp> for more information). Features of
'TCGAretriever' include: 1) it is very simple to use (get all the TCGA
data you need with a few lines of code); 2) performance (smooth and
reliable data download via 'httr'); 3) it is tailored for downloading
large volumes of data.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
