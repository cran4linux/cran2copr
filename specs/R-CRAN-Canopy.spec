%global packname  Canopy
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Accessing Intra-Tumor Heterogeneity and Tracking Longitudinaland Spatial Clonal Evolutionary History by Next-GenerationSequencing

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
A statistical framework and computational procedure for identifying the
sub-populations within a tumor, determining the mutation profiles of each
subpopulation, and inferring the tumor's phylogenetic history. The input
are variant allele frequencies (VAFs) of somatic single nucleotide
alterations (SNAs) along with allele-specific coverage ratios between the
tumor and matched normal sample for somatic copy number alterations
(CNAs). These quantities can be directly taken from the output of existing
software. Canopy provides a general mathematical framework for pooling
data across samples and sites to infer the underlying parameters. For SNAs
that fall within CNA regions, Canopy infers their temporal ordering and
resolves their phase.  When there are multiple evolutionary configurations
consistent with the data, Canopy outputs all configurations along with
their confidence assessment.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
