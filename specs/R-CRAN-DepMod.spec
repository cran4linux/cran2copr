%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DepMod
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Decision-Analytic Modelling for Depression Prevention and Treatment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-here 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-here 

%description
Provides functions and example datasets to run a decision-analytic model
for prevention and treatment strategies across depression severity states
(sub-clinical, mild, moderate, severe, and recurrent). The package
supports scenario analyses (base and alternative inputs) and summarises
outcomes such as coverage, adherence, effect sizes, and healthcare costs.

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
