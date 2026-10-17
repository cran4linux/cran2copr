%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tramnet
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Transformation Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CVXR >= 1.8
BuildRequires:    R-CRAN-tram >= 1.4
BuildRequires:    R-CRAN-mlr3mbo >= 1.2.0
BuildRequires:    R-CRAN-bbotk >= 1.0.0
BuildRequires:    R-CRAN-paradox >= 1.0.0
BuildRequires:    R-CRAN-mlt 
BuildRequires:    R-CRAN-basefun 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-lgr 
Requires:         R-CRAN-CVXR >= 1.8
Requires:         R-CRAN-tram >= 1.4
Requires:         R-CRAN-mlr3mbo >= 1.2.0
Requires:         R-CRAN-bbotk >= 1.0.0
Requires:         R-CRAN-paradox >= 1.0.0
Requires:         R-CRAN-mlt 
Requires:         R-CRAN-basefun 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lhs 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-lgr 

%description
Partially penalized versions of specific transformation models implemented
in package 'mlt'. Available models include a fully parametric version of
the Cox model, other parametric survival models (Weibull, etc.), normal
and transformed-normal (Box-Cox type) linear models, and continuous
outcome logistic regression. Models can be specified via a formula
interface. Hyperparameter tuning is facilitated through model-based
optimization functionalities from package 'mlr3mbo'. The accompanying
vignette describes the methodology used in 'tramnet' in detail.
Transformation models and model-based optimization are described in
Hothorn et al. (2019) <doi:10.1111/sjos.12291> and Bischl et al. (2017)
<doi:10.48550/arXiv.1703.03373>, respectively.

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
