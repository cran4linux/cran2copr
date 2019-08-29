%global packname  BCSub
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          A Bayesian Semiparametric Factor Analysis Model for SubtypeIdentification (Clustering)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-CRAN-nFactors >= 2.3.3
BuildRequires:    R-CRAN-mcclust >= 1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-MASS >= 7.3.45
Requires:         R-CRAN-nFactors >= 2.3.3
Requires:         R-CRAN-mcclust >= 1.0
Requires:         R-CRAN-Rcpp >= 0.12.6

%description
Gene expression profiles are commonly utilized to infer disease subtypes
and many clustering methods can be adopted for this task. However,
existing clustering methods may not perform well when genes are highly
correlated and many uninformative genes are included for clustering. To
deal with these challenges, we develop a novel clustering method in the
Bayesian setting. This method, called BCSub, adopts an innovative
semiparametric Bayesian factor analysis model to reduce the dimension of
the data to a few factor scores for clustering. Specifically, the factor
scores are assumed to follow the Dirichlet process mixture model in order
to induce clustering.

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
%{rlibdir}/%{packname}/libs
