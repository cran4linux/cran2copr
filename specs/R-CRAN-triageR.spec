%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  triageR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Machine Learning and AI Agent Tools for Clinical Prediction Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ellmer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-naniar 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ellmer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-naniar 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-yardstick 

%description
Provides a streamlined workflow for building, validating, and reporting
clinical prediction models. Combines standard machine learning tools with
an optional AI agent that recommends appropriate statistical methods, runs
sensitivity analyses, and flags common pitfalls. Includes automated
generation of reports aligned with TRIPOD+AI reporting guidance (Collins
et al. (2024 <doi:10.1136/bmj-2023-078378>)) for reproducible,
guideline-aligned research.

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
