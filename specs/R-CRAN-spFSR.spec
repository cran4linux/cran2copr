%global packname  spFSR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Feature Selection and Ranking by Simultaneous PerturbationStochastic Approximation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-class >= 7.3
BuildRequires:    R-parallel >= 3.4.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-mlr >= 2.11
BuildRequires:    R-CRAN-mlbench >= 2.1
BuildRequires:    R-CRAN-parallelMap >= 1.3
BuildRequires:    R-CRAN-tictoc >= 1.0
Requires:         R-class >= 7.3
Requires:         R-parallel >= 3.4.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-mlr >= 2.11
Requires:         R-CRAN-mlbench >= 2.1
Requires:         R-CRAN-parallelMap >= 1.3
Requires:         R-CRAN-tictoc >= 1.0

%description
An implementation of feature selection and ranking via simultaneous
perturbation stochastic approximation (SPSA-FSR) based on works by V.
Aksakalli and M. Malekipirbazari (2015) <arXiv:1508.07630> and Zeren D.
Yenice and et al. (2018) <arXiv:1804.05589>. The SPSA-FSR algorithm
searches for a locally optimal set of features that yield the best
predictive performance using a specified error measure such as mean
squared error (for regression problems) and accuracy rate (for
classification problems). This package requires an object of class 'task'
and an object of class 'Learner' from the 'mlr' package.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
