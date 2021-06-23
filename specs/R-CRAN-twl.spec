%global __brp_check_rpaths %{nil}
%global packname  twl
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Two-Way Latent Structure Clustering Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-Rfast 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-Rfast 

%description
Implementation of a Bayesian two-way latent structure model for
integrative genomic clustering.  The model clusters samples in relation to
distinct data sources, with each subject-dataset receiving a latent
cluster label, though cluster labels have across-dataset meaning because
of the model formulation.  A common scaling across data sources is
unneeded, and inference is obtained by a Gibbs Sampler.  The model can fit
multivariate Gaussian distributed clusters or a heavier-tailed
modification of a Gaussian density.  Uniquely among integrative clustering
models, the formulation makes no nestedness assumptions of samples across
data sources -- the user can still fit the model if a study subject only
has information from one data source. The package provides a variety of
post-processing functions for model examination including ones for
quantifying observed alignment of clusterings across genomic data sources.
Run time is optimized so that analyses of datasets on the order of
thousands of features on fewer than 5 datasets and hundreds of subjects
can converge in 1 or 2 days on a single CPU.  See "Swanson DM, Lien T,
Bergholtz H, Sorlie T, Frigessi A, Investigating Coordinated Architectures
Across Clusters in Integrative Studies: a Bayesian Two-Way Latent
Structure Model, 2018, <doi:10.1101/387076>, Cold Spring Harbor
Laboratory" at
<https://www.biorxiv.org/content/early/2018/08/07/387076.full.pdf> for
model details.

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
%{rlibdir}/%{packname}/INDEX
