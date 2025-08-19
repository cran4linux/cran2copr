%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtregression
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Creating Publication-Ready Regression Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-risks 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-broom.helpers 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-risks 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-broom.helpers 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 

%description
Simplifies regression modeling in R by integrating multiple modeling and
summarization tools into a cohesive, user-friendly interface. Designed to
be accessible for researchers, particularly those in Low- and
Middle-Income Countries (LMIC). Built upon widely accepted statistical
methods, including logistic regression (Hosmer et al. 2013,
ISBN:9781118548429), log-binomial regression (Spiegelman and Hertzmark
2005 <doi:10.1093/aje/kwi188>), Poisson and robust Poisson regression (Zou
2004 <doi:10.1093/aje/kwh090>), negative binomial regression (Hilbe 2011,
ISBN:9780521179515), and linear regression (Kutner et al. 2005,
ISBN:9780071122214). Leverages multiple dependencies to ensure
high-quality output and generate reproducible, publication-ready tables in
alignment with best practices in epidemiology and applied statistics.

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
