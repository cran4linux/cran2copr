%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  viralx
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explainers for Regression Models in HIV Research

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-DALEXtra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-plotmo 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-vdiffr 
BuildRequires:    R-CRAN-workflows 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-DALEXtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-plotmo 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-vdiffr 
Requires:         R-CRAN-workflows 

%description
A dedicated viral-explainer model tool designed to empower researchers in
the field of HIV research, particularly in viral load and CD4 (Cluster of
Differentiation 4) lymphocytes regression modeling. Drawing inspiration
from the 'tidymodels' framework for rigorous model building of Max Kuhn
and Hadley Wickham (2020) <https://www.tidymodels.org>, and the 'DALEXtra'
tool for explainability by Przemyslaw Biecek (2020) <arXiv:2009.13248>. It
aims to facilitate interpretable and reproducible research in
biostatistics and computational biology for the benefit of understanding
HIV dynamics.

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
