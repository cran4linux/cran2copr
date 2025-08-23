%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exams.forge
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Support for Compiling Examination Tasks using the 'exams' Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-spelling 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stranslate 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-yaml 
Requires:         R-tools 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-spelling 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stranslate 
Requires:         R-CRAN-tinytex 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-yaml 

%description
The main aim is to further facilitate the creation of exercises based on
the package 'exams' by Grün, B., and Zeileis, A. (2009)
<doi:10.18637/jss.v029.i10>. Creating effective student exercises involves
challenges such as creating appropriate data sets and ensuring access to
intermediate values for accurate explanation of solutions. The
functionality includes the generation of univariate and bivariate data
including simple time series, functions for theoretical distributions and
their approximation, statistical and mathematical calculations for tasks
in basic statistics courses as well as general tasks such as string
manipulation, LaTeX/HTML formatting and the editing of XML task files for
'Moodle'.

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
