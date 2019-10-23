%global packname  whoa
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Evaluation of Genotyping Error in Genotype-by-Sequencing Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vcfR 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vcfR 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 

%description
This is a small, lightweight package that lets users investigate the
distribution of genotypes in genotype-by-sequencing (GBS) data where they
expect (by and large) Hardy-Weinberg equilibrium, in order to assess rates
of genotyping errors and the dependence of those rates on read depth.  It
implements a Markov chain Monte Carlo (MCMC) sampler using 'Rcpp' to
compute a Bayesian estimate of what we call the heterozygote miscall rate
for restriction-associated digest (RAD) sequencing data and other types of
reduced representation GBS data. It also provides functions to generate
plots of expected and observed genotype frequencies. Some background on
these topics can be found in a recent paper "Recent advances in
conservation and population genomics data analysis" by Hendricks et al.
(2018) <doi:10.1111/eva.12659>, and another paper describing the MCMC
approach is in preparation with Gordon Luikart and Thierry Gosselin.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
