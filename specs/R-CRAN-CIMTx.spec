%global packname  CIMTx
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Causal Inference for Multiple Treatments with a Binary Outcome

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Matching 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-WeightIt 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-tmle 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-gam 
Requires:         R-nnet 
Requires:         R-CRAN-BART 
Requires:         R-CRAN-twang 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Matching 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-WeightIt 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-tmle 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-class 
Requires:         R-CRAN-gam 

%description
Different methods to conduct causal inference for multiple treatments with
a binary outcome, including regression adjustment, vector matching,
Bayesian additive regression trees, targeted maximum likelihood and
inverse probability of treatment weighting using different generalized
propensity score models such as multinomial logistic regression,
generalized boosted models and super learner. For more details, see the
paper by Liangyuan Hu (2020) <arXiv:2001.06483> and Jennifer L. Hill
(2011) <doi:10.1198/jcgs.2010.08162>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
