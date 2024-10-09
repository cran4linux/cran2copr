%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pubh
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolbox for Public Health and Epidemiology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jtools 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-sjlabelled 
BuildRequires:    R-CRAN-sjmisc 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggformula 
Requires:         R-stats 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Epi 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jtools 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-sjlabelled 
Requires:         R-CRAN-sjmisc 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
A toolbox for making R functions and capabilities more accessible to
students and professionals from Epidemiology and Public Health related
disciplines. Includes a function to report coefficients and confidence
intervals from models using robust standard errors (when available),
functions that expand 'ggplot2' plots and functions relevant for
introductory papers in Epidemiology or Public Health. Please note that use
of the provided data sets is for educational purposes only.

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
