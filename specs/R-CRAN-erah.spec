%global packname  erah
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Automated Spectral Deconvolution, Alignment, and MetaboliteIdentification in GC/MS-Based Untargeted Metabolomics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-XML 
Requires:         R-methods 

%description
Automated compound deconvolution, alignment across samples, and
identification of metabolites by spectral library matching in Gas
Chromatography - Mass spectrometry (GC-MS) untargeted metabolomics.
Outputs a table with compound names, matching scores and the integrated
area of the compound for each sample. Package implementation is described
in Domingo-Almenara et al. (2016) <doi:10.1021/acs.analchem.6b02927>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
