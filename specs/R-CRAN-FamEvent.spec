%global __brp_check_rpaths %{nil}
%global packname  FamEvent
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Family Age-at-Onset Data Simulation and Penetrance Estimation

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-eha 
Requires:         R-CRAN-pracma 

%description
Simulates age-at-onset traits associated with a segregating major gene in
family data obtained from population-based, clinic-based, or multi-stage
designs. Appropriate ascertainment correction is utilized to estimate
age-dependent penetrance functions either parametrically from the fitted
model or nonparametrically from the data. The Expectation and Maximization
algorithm can infer missing genotypes and carrier probabilities estimated
from family's genotype and phenotype information or from a fitted model.
Plot functions include pedigrees of simulated families and predicted
penetrance curves based on specified parameter values. For more
information see Choi, Y.-H., Briollais, L., He, W. and Kopciuk, K. (2021)
FamEvent: An R Package for Generating and Modeling Time-to-Event Data in
Family Designs, Journal of Statistical Software 97 (7), 1-30.
<doi:10.18637/jss.v097.i07>.

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
