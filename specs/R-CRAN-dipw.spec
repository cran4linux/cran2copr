%global packname  dipw
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Debiased Inverse Propensity Score Weighting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Rmosek 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Rmosek 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 

%description
Estimation of the average treatment effect when controlling for
high-dimensional confounders using debiased inverse propensity score
weighting (DIPW). DIPW relies on the propensity score following a sparse
logistic regression model, but the regression curves are not required to
be estimable. Despite this, our package also allows the users to estimate
the regression curves and take the estimated curves as input to our
methods. Details of the methodology can be found in Yuhao Wang and Rajen
D. Shah (2020) "Debiased Inverse Propensity Score Weighting for Estimation
of Average Treatment Effects with High-Dimensional Confounders"
<arXiv:2011.08661>. The package relies on the optimisation software
'MOSEK' <https://www.mosek.com/> which must be installed separately; see
the documentation for 'Rmosek'.

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
