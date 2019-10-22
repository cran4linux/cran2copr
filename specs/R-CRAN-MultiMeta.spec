%global packname  MultiMeta
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Meta-analysis of Multivariate Genome Wide Association Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-gtable 
Requires:         R-grid 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Allows running a meta-analysis of multivariate Genome Wide Association
Studies (GWAS) and easily visualizing results through custom plotting
functions. The multivariate setting implies that results for each single
nucleotide polymorphism (SNP) include several effect sizes (also known as
"beta coefficients", one for each trait), as well as related variance
values, but also covariance between the betas. The main goal of the
package is to provide combined beta coefficients across different cohorts,
together with the combined variance/covariance matrix. The method is
inverse-variance based, thus each beta is weighted by the inverse of its
variance-covariance matrix, before taking the average across all betas.
The default options of the main function code{multi_meta} will work with
files obtained from GEMMA multivariate option for GWAS (Zhou & Stephens,
2014). It will work with any other output, as soon as columns are
formatted to have the according names. The package also provides several
plotting functions for QQ-plots, Manhattan Plots and custom summary plots.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
