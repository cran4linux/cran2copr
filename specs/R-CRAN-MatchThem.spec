%global packname  MatchThem
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Matching and Weighting Multiply Imputed Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MatchIt >= 4.0.0
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-WeightIt 
Requires:         R-CRAN-MatchIt >= 4.0.0
Requires:         R-CRAN-mice 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-WeightIt 

%description
Provides the necessary tools for the pre-processing techniques of matching
and weighting multiply imputed datasets to control for effects of
confounders and to reduce the degree of dependence on certain modeling
assumptions in studying the causal associations between an exposure and an
outcome. This package includes functions to perform matching within and
across the multiply imputed datasets using several matching methods, to
estimate weights of units in the imputed datasets using several weighting
methods, to calculate the causal effect estimate in each matched or
weighted dataset using parametric or non-parametric statistical models,
and to pool the obtained estimates from these models according to Rubin's
rules (please see <https://github.com/FarhadPishgar/MatchThem> for
details).

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
