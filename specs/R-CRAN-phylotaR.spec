%global packname  phylotaR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Automated Phylogenetic Sequence Cluster Identification from'GenBank'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         ncbi-blast+ >= 2.0
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rentrez 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-CRAN-treeman 
BuildRequires:    R-CRAN-treemapify 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rentrez 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sys 
Requires:         R-CRAN-treeman 
Requires:         R-CRAN-treemapify 
Requires:         R-CRAN-R.utils 

%description
A pipeline for the identification, within taxonomic groups, of orthologous
sequence clusters from 'GenBank' <https://www.ncbi.nlm.nih.gov/genbank/>
as the first step in a phylogenetic analysis. The pipeline depends on a
local alignment search tool and is, therefore, not dependent on
differences in gene naming conventions and naming errors.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
