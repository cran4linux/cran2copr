%global __brp_check_rpaths %{nil}
%global packname  gorica
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation of Inequality Constrained Hypotheses Using GORICA

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bain >= 0.2.2
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-limSolve 
Requires:         R-CRAN-bain >= 0.2.2
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-limSolve 

%description
Implements the generalized order-restricted information criterion
approximation (GORICA) by Kuiper, Hoijtink, & Silvapulle (2012)
<doi:10.1016/j.jspi.2012.03.007>. The GORICA is an AIC-like information
criterion that can be utilized to evaluate informative hypotheses
specifying directional relationships between model parameters in terms of
(in)equality constraints. The GORICA is applicable not only to normal
linear models, but also to generalized linear models (GLMs), generalized
linear mixed models (GLMMs), and structural equation models (SEMs). In
addition, the GORICA can be utilized in the context of contingency tables
for which (in)equality constrained hypotheses do not necessarily contain
linear restrictions on cell probabilities, but instead often contain
non-linear restrictions on cell probabilities.

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
