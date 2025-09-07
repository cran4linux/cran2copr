%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pre
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction Rule Ensembles

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit >= 1.2.0
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MatrixModels 
Requires:         R-CRAN-partykit >= 1.2.0
Requires:         R-CRAN-earth 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MatrixModels 

%description
Derives prediction rule ensembles (PREs). Largely follows the procedure
for deriving PREs as described in Friedman & Popescu (2008;
<DOI:10.1214/07-AOAS148>), with adjustments and improvements described in
Fokkema (2020; <DOI:10.18637/jss.v092.i12>) and Fokkema & Strobl (2020;
<DOI:10.1037/met0000256>). The main function pre() derives prediction rule
ensembles consisting of rules and/or linear terms for continuous, binary,
count, multinomial, survival and multivariate continuous responses.
Function gpe() derives generalized prediction ensembles, consisting of
rules, hinge and linear functions of the predictor variables.

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
