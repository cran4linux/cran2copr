%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IMIFA
%global packver   2.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Infinite Mixtures of Infinite Factor Analysers and Related Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust >= 5.4
BuildRequires:    R-CRAN-Rfast >= 1.9.8
BuildRequires:    R-CRAN-matrixStats >= 0.53.1
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-mclust >= 5.4
Requires:         R-CRAN-Rfast >= 1.9.8
Requires:         R-CRAN-matrixStats >= 0.53.1
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-viridisLite 

%description
Provides flexible Bayesian estimation of Infinite Mixtures of Infinite
Factor Analysers and related models, for nonparametrically clustering
high-dimensional data, introduced by Murphy et al. (2020)
<doi:10.1214/19-BA1179>. The IMIFA model conducts Bayesian nonparametric
model-based clustering with factor analytic covariance structures without
recourse to model selection criteria to choose the number of clusters or
cluster-specific latent factors, mostly via efficient Gibbs updates.
Model-specific diagnostic tools are also provided, as well as many options
for plotting results, conducting posterior inference on parameters of
interest, posterior predictive checking, and quantifying uncertainty.

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
