%global packname  BayesVarSel
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Bayes Factors, Model Choice and Variable Selection in LinearModels

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-parallel >= 3.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0.5
Requires:         R-MASS >= 7.3.45
Requires:         R-parallel >= 3.3
Requires:         R-CRAN-mvtnorm >= 1.0.5

%description
Conceived to calculate Bayes factors in Linear models and then to provide
a formal Bayesian answer to testing and variable selection problems. From
a theoretical side, the emphasis in this package is placed on the prior
distributions and it allows a wide range of them: Jeffreys (1961); Zellner
and Siow(1980)<DOI:10.1007/bf02888369>; Zellner and Siow(1984); Zellner
(1986)<DOI:10.2307/2233941>; Fernandez et al.
(2001)<DOI:10.1016/s0304-4076(00)00076-2>; Liang et al.
(2008)<DOI:10.1198/016214507000001337> and Bayarri et al.
(2012)<DOI:10.1214/12-aos1013>. The interaction with the package is
through a friendly interface that syntactically mimics the well-known lm()
command of R. The resulting objects can be easily explored providing the
user very valuable information (like marginal, joint and conditional
inclusion probabilities of potential variables; the highest posterior
probability model, HPM; the median probability model, MPM) about the
structure of the true -data generating- model. Additionally, this package
incorporates abilities to handle problems with a large number of potential
explanatory variables through parallel and heuristic versions of the main
commands, Garcia-Donato and Martinez-Beneito
(2013)<DOI:10.1080/01621459.2012.742443>. It also allows problems with p>n
and p>>n and also incorporates routines to handle problems with variable
selection with factors.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
