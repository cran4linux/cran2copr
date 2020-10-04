%global packname  BClustLonG
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          A Dirichlet Process Mixture Model for Clustering LongitudinalGene Expression Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-CRAN-lme4 >= 1.1.13
BuildRequires:    R-CRAN-mcclust >= 1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-MASS >= 7.3.47
Requires:         R-CRAN-lme4 >= 1.1.13
Requires:         R-CRAN-mcclust >= 1.0
Requires:         R-CRAN-Rcpp >= 0.12.7

%description
Many clustering methods have been proposed, but most of them cannot work
for longitudinal gene expression data. 'BClustLonG' is a package that
allows us to perform clustering analysis for longitudinal gene expression
data. It adopts a linear-mixed effects framework to model the trajectory
of genes over time, while clustering is jointly conducted based on the
regression coefficients obtained from all genes. To account for the
correlations among genes and alleviate the high dimensionality challenges,
factor analysis models are adopted for the regression coefficients. The
Dirichlet process prior distribution is utilized for the means of the
regression coefficients to induce clustering. This package allows users to
specify which variables to use for clustering (intercepts or slopes or
both) and whether a factor analysis model is desired. More details about
this method can be found in Jiehuan Sun, et al. (2017)
<doi:10.1002/sim.7374>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/libs
