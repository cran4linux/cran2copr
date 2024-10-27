%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmm.hp
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Partitioning of Marginal R2 for Generalized Mixed-Effect Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-lme4 

%description
Conducts hierarchical partitioning to calculate individual contributions
of each predictor (fixed effects) towards marginal R2 for generalized
linear mixed-effect model (including lm, glm and glmm) based on output of
r.squaredGLMM() in 'MuMIn', applying the algorithm of Lai J.,Zou Y., Zhang
S.,Zhang X.,Mao L.(2022)glmm.hp: an R package for computing individual
effect of predictors in generalized linear mixed models.Journal of Plant
Ecology,15(6)1302-1307<doi:10.1093/jpe/rtac096>.

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
