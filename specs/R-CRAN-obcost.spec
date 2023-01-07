%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  obcost
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Obesity Cost Database

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 

%description
This database contains necessary data relevant to medical costs on obesity
throughout the United States. This database, in form of an R package,
could output necessary data frames relevant to obesity costs, where the
clients could easily manipulate the output using difference parameters,
e.g. relative risks for each illnesses. This package contributes to parts
of our published journal named "Modeling the Economic Cost of Obesity Risk
and Its Relation to the Health Insurance Premium in the United States: A
State Level Analysis". Please use the following citation for the journal:
Woods Thomas, Tatjana Miljkovic (2022) "Modeling the Economic Cost of
Obesity Risk and Its Relation to the Health Insurance Premium in the
United States: A State Level Analysis" <doi:10.3390/risks10100197>. The
database is composed of the following main tables: 1. Relative_Risks:
(constant) Relative risks for a given disease group with a risk factor of
obesity; 2. Disease_Cost: (obesity_cost_disease) Supplementary output with
all variables related to individual disease groups in a given state and
year; 3. Full_Cost: (obesity_cost_full) Complete output with all variables
used to make cost calculations, as well as cost calculations in a given
state and year; 4. National_Summary: (obesity_cost_national_summary)
National summary cost calculations in a given year. Three functions are
included to assist users in calling and adjusting the mentioned tables and
they are data_load(), data_produce(), and rel_risk_fun().

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
