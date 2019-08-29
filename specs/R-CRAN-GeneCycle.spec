%global packname  GeneCycle
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Identification of Periodically Expressed Genes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fdrtool >= 1.2.5
BuildRequires:    R-CRAN-longitudinal >= 1.1.3
BuildRequires:    R-MASS 
Requires:         R-CRAN-fdrtool >= 1.2.5
Requires:         R-CRAN-longitudinal >= 1.1.3
Requires:         R-MASS 

%description
The GeneCycle package implements the approaches of Wichert et al. (2004)
<doi.org/10.1093/bioinformatics/btg364>, Ahdesmaki et al. (2005)
<DOI:10.1186/1471-2105-6-117> and Ahdesmaki et al. (2007)
<DOI:10.1186/1471-2105-8-233> for detecting periodically expressed genes
from gene expression time series data.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
