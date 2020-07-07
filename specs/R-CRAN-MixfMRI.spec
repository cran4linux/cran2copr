%global packname  MixfMRI
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Mixture fMRI Clustering Analysis

License:          Mozilla Public License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-CRAN-MixSim 
BuildRequires:    R-CRAN-EMCluster 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-fftw 
Requires:         R-CRAN-MixSim 
Requires:         R-CRAN-EMCluster 

%description
Utilizing model-based clustering (unsupervised) for functional magnetic
resonance imaging (fMRI) data. The developed methods (Chen and Maitra
(2018, manuscript)) include 2D and 3D clustering analyses (for p-values
with voxel locations) and segmentation analyses (for p-values alone) for
fMRI data where p-values indicate significant level of activation
responding to stimulate of interesting. The analyses are mainly
identifying active voxel/signal associated with normal brain behaviors.
Analysis pipelines (R scripts) utilizing this package (see examples in
'inst/workflow/') is also implemented with high performance techniques.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/workflow
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
