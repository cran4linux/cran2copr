%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  esem
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Structural Equation Modeling ESEM

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-utils 

%description
A collection of functions developed to support the tutorial on using
Exploratory Structural Equiation Modeling (ESEM) (Asparouhov & Muthén,
2009) <https://www.statmodel.com/download/EFACFA810.pdf>) with
Longitudinal Study of Australian Children (LSAC) dataset (Mohal et al.,
2023) <doi:10.26193/QR4L6Q>. The package uses 'tidyverse','psych',
'lavaan','semPlot' and provides additional functions to conduct ESEM. The
package provides general functions to complete ESEM, including esem_c(),
creation of target matrix (if it is used) make_target(), generation of the
Confirmatory Factor Analysis (CFA) model syntax esem_cfa_syntax(). A
sample data is provided - the package includes a sample data of the
Strengths and Difficulties Questionnaire of the Longitudinal Study of
Australian Children (SDQ LSAC) in sdq_lsac(). 'ESEM' package vignette
presents the tutorial demonstrating the use of ESEM on SDQ LSAC data.

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
