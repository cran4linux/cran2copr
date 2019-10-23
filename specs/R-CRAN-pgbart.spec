%global packname  pgbart
%global packver   0.6.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.16
Release:          1%{?dist}
Summary:          Bayesian Additive Regression Trees Using Particle Gibbs Samplerand Gibbs/Metropolis-Hastings Sampler

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-BayesTree >= 0.3.1.4
Requires:         R-CRAN-BayesTree >= 0.3.1.4

%description
The Particle Gibbs sampler and Gibbs/Metropolis-Hastings sampler were
implemented to fit Bayesian additive regression tree model. Construction
of the model (training) and prediction for a new data set (testing) can be
separated. Our reference papers are: Lakshminarayanan B, Roy D, Teh Y W.
Particle Gibbs for Bayesian additive regression trees[C], Artificial
Intelligence and Statistics. 2015: 553-561,
<http://proceedings.mlr.press/v38/lakshminarayanan15.pdf> and Chipman, H.,
George, E., and McCulloch R. (2010) Bayesian Additive Regression Trees.
The Annals of Applied Statistics, 4,1, 266-298, <doi:10.1214/09-aoas285>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
