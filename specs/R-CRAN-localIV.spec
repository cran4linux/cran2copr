%global packname  localIV
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Estimation of Marginal Treatment Effects using LocalInstrumental Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-KernSmooth >= 2.5.0
BuildRequires:    R-mgcv >= 1.8.19
BuildRequires:    R-CRAN-sampleSelection >= 1.2.0
BuildRequires:    R-stats 
Requires:         R-KernSmooth >= 2.5.0
Requires:         R-mgcv >= 1.8.19
Requires:         R-CRAN-sampleSelection >= 1.2.0
Requires:         R-stats 

%description
In the generalized Roy model, the marginal treatment effect (MTE) can be
used as a building block for constructing conventional causal parameters
such as the average treatment effect (ATE) and the average treatment
effect on the treated (ATT) (Heckman, Urzua, and Vytlacil 2006
<doi:10.1162/rest.88.3.389>). Given a treatment selection model and an
outcome model, the function mte() estimates the MTE via a semiparametric
local instrumental variables method (or via a normal selection model). The
function eval_mte() evaluates MTE at any combination of covariates x and
latent resistance u, and the function eval_mte_tilde() evaluates MTE
projected onto the estimated propensity score (Zhou and Xie 2019
<https://www.journals.uchicago.edu/doi/abs/10.1086/702172>). The object
returned by mte() can be used to estimate conventional parameters such as
ATE and ATT (via average()) or marginal policy-relevant treatment effects
(via mprte()).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
