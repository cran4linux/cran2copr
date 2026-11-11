%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StabilityApp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Stability Analysis of Multi-Environment Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-stability >= 1.0.0
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
Requires:         R-CRAN-stability >= 1.0.0
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-shiny 
Requires:         R-utils 

%description
A 'shiny' application for the stability analysis of multi-environment
trials of plant breeding with the package 'stability': analyses of
variance, Eberhart and Russell's and Finlay and Wilkinson's regression,
Wricke's, Shukla's, Kang's and Fox's statistics, Eskridge's safety-first
indices, Annicchiarico's, Lin and Binns' and Huehn's statistics, AMMI
analysis and stability values, and the GGE biplot. Every analysis comes
with its tables, plots, the R code that repeats it and an interpretation
specific to the method, computed from the results; an optional longer
written interpretation can be requested from an external text service with
the user's own key.

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
