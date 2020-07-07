%global packname  SequenceSpikeSlab
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Exact Bayesian Model Selection Methods for the Sparse NormalSequence Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-selectiveInference >= 1.2.5
BuildRequires:    R-CRAN-RcppProgress >= 0.4.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-selectiveInference >= 1.2.5
Requires:         R-CRAN-RcppProgress >= 0.4.1
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
Contains fast functions to calculate the exact Bayes posterior for the
Sparse Normal Sequence Model, which implement the algorithms described in
Van Erven and Szabo (2018) <arXiv:1810.10883>. For general hierarchical
priors, sample sizes up to 10,000 are feasible within half an hour on a
standard laptop. For beta-binomial spike-and-slab priors, a faster
algorithm is provided, which can handle sample sizes of 100,000 in half an
hour. In the implementation, special care has been taken to assure
numerical stability of the methods even for such large sample sizes.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
