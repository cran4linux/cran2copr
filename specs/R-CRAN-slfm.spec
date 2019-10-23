%global packname  slfm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Tools for Fitting Sparse Latent Factor Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-coda 
Requires:         R-lattice 

%description
Set of tools to find coherent patterns in microarray data using a Bayesian
Sparse Latent Factor Model - SLFM; see Duarte and Mayrink (2015)
<DOI:10.1007/978-3-319-12454-4_15>. Considerable effort has been put into
making slfm fast and memory efficient, turning it an interesting
alternative to simpler methods in terms of execution time. It implements
versions of the SLFM based on two type of mixtures priors for the
loadings: one relying on a degenerate component at zero and the other
using a small variance normal distribution for the spike part of the
mixture. It also implements additional functions to allow pre-processing
procedures for the data and to fit the model for a large number of
probesets or genes.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
