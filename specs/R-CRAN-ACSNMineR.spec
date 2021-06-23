%global __brp_check_rpaths %{nil}
%global packname  ACSNMineR
%global packver   0.16.8.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.8.25
Release:          3%{?dist}%{?buildtag}
Summary:          Gene Enrichment Analysis from ACSN Maps or GMT Files

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 

%description
Compute and represent gene set enrichment or depletion from your data
based on pre-saved maps from the Atlas of Cancer Signalling Networks
(ACSN) or user imported maps. User imported maps must be complying with
the GMT format as defined by the Broad Institute, that is to say that the
file should be tab- separated, that the first column should contain the
module name, the second column can contain comments that will be
overwritten with the number of genes in the module, and subsequent columns
must contain the list of genes (HUGO symbols; tab-separated) inside the
module. The gene set enrichment can be run with hypergeometric test or
Fisher exact test, and can use multiple corrections. Visualization of data
can be done either by barplots or heatmaps.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
