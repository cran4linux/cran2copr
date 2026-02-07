%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmixr2auto
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Population Pharmacokinetic Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-processx > 3.8.0
BuildRequires:    R-CRAN-nlmixr2data 
BuildRequires:    R-CRAN-nlmixr2 
BuildRequires:    R-CRAN-nlmixr2est 
BuildRequires:    R-CRAN-nlmixr2autoinit 
BuildRequires:    R-CRAN-rxode2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-processx > 3.8.0
Requires:         R-CRAN-nlmixr2data 
Requires:         R-CRAN-nlmixr2 
Requires:         R-CRAN-nlmixr2est 
Requires:         R-CRAN-nlmixr2autoinit 
Requires:         R-CRAN-rxode2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-crayon 

%description
Automated population pharmacokinetic modeling framework for data-driven
initialisation, model evaluation, and metaheuristic optimization. Supports
genetic algorithms, ant colony optimization, tabu search, and stepwise
procedures for automated model selection and parameter estimation within
the nlmixr2 ecosystem.

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
