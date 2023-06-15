%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MatchThem
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
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
Provides essential tools for the pre-processing techniques of matching and
weighting multiply imputed datasets. The package includes functions for
matching within and across multiply imputed datasets using various
methods, estimating weights for units in the imputed datasets using
multiple weighting methods, calculating causal effect estimates in each
matched or weighted dataset using parametric or non-parametric statistical
models, and pooling the resulting estimates according to Rubin's rules
(please see <https://journal.r-project.org/archive/2021/RJ-2021-073/> for
more details).

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
