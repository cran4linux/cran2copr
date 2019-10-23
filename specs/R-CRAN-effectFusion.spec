%global packname  effectFusion
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Bayesian Effect Fusion for Categorical Predictors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-mcclust 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-bayesm 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-GreedyEPL 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-mcclust 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-bayesm 
Requires:         R-cluster 
Requires:         R-CRAN-GreedyEPL 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Variable selection and Bayesian effect fusion for categorical predictors
in linear and logistic regression models. Effect fusion aims at the
question which categories have a similar effect on the response and
therefore can be fused to obtain a sparser representation of the model.
Effect fusion and variable selection can be obtained either with a prior
that has an interpretation as spike and slab prior on the level effect
differences or with a sparse finite mixture prior on the level effects.
The regression coefficients are estimated with a flat uninformative prior
after model selection or by taking model averages. Posterior inference is
accomplished by an MCMC sampling scheme which makes use of a data
augmentation strategy (Polson, Scott & Windle (2013)) based on latent
Polya-Gamma random variables in the case of logistic regression. The code
for data augmentation is taken from Polson et al. (2013), who own the
copyright.

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
%{rlibdir}/%{packname}/libs
