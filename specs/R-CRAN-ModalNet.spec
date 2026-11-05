%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ModalNet
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Parametric Modal Regression: Lasso, Elastic Net and Ridge

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-graphics 

%description
Variable selection and estimation for parametric modal regression with
continuous positive responses (Gamma, Weibull and Lognormal families)
under Lasso, elastic-net, ridge and adaptive-Lasso penalties. The
conditional mode is linked to a linear predictor through a logarithmic
link using the mode reparameterization of Galarza and Lachos (2026)
<doi:10.48550/arXiv.2603.07099>. The penalized log-likelihood is maximized
with a proximal Newton algorithm (iteratively reweighted penalized least
squares): at each iteration the modal log-likelihood is replaced by a
local quadratic surrogate in the linear predictor, which yields a
pseudo-response and a working weight in closed form, and the resulting
weighted penalized least-squares subproblem is solved by the
coordinate-descent solver of 'glmnet' (Friedman, Hastie and Tibshirani,
2010, <doi:10.18637/jss.v033.i01>). The regularization parameter is chosen
along a warm-started path by the extended Bayesian information criterion
of Chen and Chen (2008) <doi:10.1093/biomet/asn034>.

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
