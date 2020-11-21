%global packname  MetaIntegration
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble Meta-Prediction Framework

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-knitr 

%description
An ensemble meta-prediction framework to integrate multiple regression
models into a current study. Gu, T., Taylor, J.M.G. and Mukherjee, B.
(2020) <arXiv:2010.09971>. A meta-analysis framework along with two
weighted estimators as the ensemble of empirical Bayes estimators, which
combines the estimates from the different external models. The proposed
framework is flexible and robust in the ways that (i) it is capable of
incorporating external models that use a slightly different set of
covariates; (ii) it is able to identify the most relevant external
information and diminish the influence of information that is less
compatible with the internal data; and (iii) it nicely balances the
bias-variance trade-off while preserving the most efficiency gain. The
proposed estimators are more efficient than the naive analysis of the
internal data and other naive combinations of external estimators.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
