%global __brp_check_rpaths %{nil}
%global packname  effectFusion
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Effect Fusion for Categorical Predictors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-mcclust 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-bayesm 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-GreedyEPL 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-mcclust 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-bayesm 
Requires:         R-CRAN-cluster 
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
augmentation strategy (Polson, Scott & Windle (2013)
<doi:10.1080/01621459.2013.829001>) based on latent Polya-Gamma random
variables in the case of logistic regression. The code for data
augmentation is taken from Polson et al. (2013)
<doi:10.1080/01621459.2013.829001>, who own the copyright.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
