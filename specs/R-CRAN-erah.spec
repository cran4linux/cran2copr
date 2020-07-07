%global packname  erah
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Automated Spectral Deconvolution, Alignment, and MetaboliteIdentification in GC/MS-Based Untargeted Metabolomics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
