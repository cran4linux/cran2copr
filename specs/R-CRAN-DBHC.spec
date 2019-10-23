%global packname  DBHC
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Sequence Clustering with Discrete-Output HMMs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-TraMineR >= 2.0.7
BuildRequires:    R-CRAN-reshape2 >= 1.2.1
BuildRequires:    R-CRAN-seqHMM >= 1.0.8
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-TraMineR >= 2.0.7
Requires:         R-CRAN-reshape2 >= 1.2.1
Requires:         R-CRAN-seqHMM >= 1.0.8

%description
Provides an implementation of a mixture of hidden Markov models (HMMs) for
discrete sequence data in the Discrete Bayesian HMM Clustering (DBHC)
algorithm. The DBHC algorithm is an HMM Clustering algorithm that finds a
mixture of discrete-output HMMs while using heuristics based on Bayesian
Information Criterion (BIC) to search for the optimal number of HMM states
and the optimal number of clusters.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
