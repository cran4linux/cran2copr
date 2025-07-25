%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pleLMA
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Pseudo-Likelihood Estimation of Log-Multiplicative Association Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-dfidx 
Requires:         R-stats 
Requires:         R-graphics 

%description
Log-multiplicative association models (LMA) are models for
cross-classifications of categorical variables where interactions are
represented by products of category scale values and an association
parameter. Maximum likelihood estimation (MLE) fails for moderate to large
numbers of categorical variables. The 'pleLMA' package overcomes this
limitation of MLE by using pseudo-likelihood estimation to fit the models
to small or large cross-classifications dichotomous or multi-category
variables. Originally proposed by Besag (1974,
<doi:10.1111/j.2517-6161.1974.tb00999.x>), pseudo-likelihood estimation
takes large complex models and breaks it down into smaller ones. Rather
than maximizing the likelihood of the joint distribution of all the
variables, a pseudo-likelihood function, which is the product likelihoods
from conditional distributions, is maximized. LMA models can be derived
from a number of different frameworks including (but not limited to)
graphical models and uni-dimensional and multi-dimensional item response
theory models. More details about the models and estimation can be found
in the vignette.

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
