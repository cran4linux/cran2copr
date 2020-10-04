%global packname  bartBMA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Additive Regression Trees using Bayesian ModelAveraging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-Rdpack 

%description
"BART-BMA Bayesian Additive Regression Trees using Bayesian Model
Averaging" (Hernandez B, Raftery A.E., Parnell A.C. (2018)
<doi:10.1007/s11222-017-9767-1>) is an extension to the original BART
sum-of-trees model (Chipman et al 2010). BART-BMA differs to the original
BART model in two main aspects in order to implement a greedy model which
will be computationally feasible for high dimensional data. Firstly
BART-BMA uses a greedy search for the best split points and variables when
growing decision trees within each sum-of-trees model. This means trees
are only grown based on the most predictive set of split rules. Also
rather than using Markov chain Monte Carlo (MCMC), BART-BMA uses a greedy
implementation of Bayesian Model Averaging called Occam's Window which
take a weighted average over multiple sum-of-trees models to form its
overall prediction. This means that only the set of sum-of-trees for which
there is high support from the data are saved to memory and used in the
final model.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
