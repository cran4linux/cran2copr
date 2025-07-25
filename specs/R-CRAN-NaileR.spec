%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NaileR
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interpreting Latent Variables with AI

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-ollamar 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-SensoMineR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-ollamar 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-SensoMineR 

%description
A small package designed for interpreting continuous and categorical
latent variables. You provide a data set with a latent variable you want
to understand and some other explanatory variables. It provides a
description of the latent variable based on the explanatory variables. It
also provides a name to the latent variable.

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
