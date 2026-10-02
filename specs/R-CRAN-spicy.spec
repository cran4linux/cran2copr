%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spicy
%global packver   0.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          Publication-Ready Tables for Descriptive Statistics and Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 3.1.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-sandwich >= 3.1.2
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-labelled 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Provides publication-ready tables for descriptive statistics and
regression models: frequency tables and cross-tabulations with association
measures (Cramer's V, Kendall's Tau-b, and others), categorical and
continuous summary tables, by group or from a complex survey design, and
regression tables for one or more models side by side, across more than
thirty model classes from mixed-effects to survival and Bayesian, with
robust standard errors, average marginal effects, and univariable
screening. Tables follow APA conventions by default, can switch to named
journal styles such as JAMA, NEJM, or The Lancet, and render identically
in the console and in 'gt', 'tinytable', 'flextable', 'Word', 'Excel', or
the clipboard. Declared missing values in labelled data are honored and
disclosed throughout the descriptive tables. Helpers cover codebooks,
variable inspection, and row-wise summaries.

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
