%global __brp_check_rpaths %{nil}
%global packname  semicmprskcoxmsm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Use Inverse Probability Weighting to Estimate Treatment Effect for Semi Competing Risks Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-twang 
Requires:         R-graphics 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-Rcpp 

%description
Use inverse probability weighting methods to estimate treatment effect
under marginal structure model (MSM) for the transition hazard of semi
competing risk data, i.e. illness death model. We implement two specific
such models, the usual Markov illness death structural model and the
general Markov illness death structural model. We also provide the
predicted three risks functions from the marginal structure models. Zhang,
Y. and Xu, R. (2022) <arXiv:2204.10426>.

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
