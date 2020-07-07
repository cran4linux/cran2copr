%global packname  MixGHD
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          3%{?dist}
Summary:          Model Based Clustering, Classification and Discriminant AnalysisUsing the Mixture of Generalized Hyperbolic Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Bessel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ghyp 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mixture 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-cluster 
BuildRequires:    R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-Bessel 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ghyp 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mixture 
Requires:         R-CRAN-e1071 
Requires:         R-cluster 
Requires:         R-methods 

%description
Carries out model-based clustering, classification and discriminant
analysis using five different models. The models are all based on the
generalized hyperbolic distribution. The first model 'MGHD' (Browne and
McNicholas (2015) <doi:10.1002/cjs.11246>) is the classical mixture of
generalized hyperbolic distributions. The 'MGHFA' (Tortora et al. (2016)
<doi:10.1007/s11634-015-0204-z>) is the mixture of generalized hyperbolic
factor analyzers for high dimensional data sets. The 'MSGHD'(Tortora et
al. (2016) <arXiv:1403.2332v7>), mixture of multiple scaled generalized
hyperbolic distributions. The 'cMSGHD' (Tortora et al. (2016)
<arXiv:1403.2332v7>) is a 'MSGHD' with convex contour plots. The 'MCGHD'
(Tortora et al. (2016) <arXiv:1403.2332v7>), mixture of coalesced
generalized hyperbolic distributions is a new more flexible model.

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
%{rlibdir}/%{packname}/libs
