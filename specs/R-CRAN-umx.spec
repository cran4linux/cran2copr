%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  umx
%global packver   4.20.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.20.0
Release:          1%{?dist}%{?buildtag}
Summary:          Structural Equation Modeling and Twin Modeling in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx >= 2.19.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-psychTools 
BuildRequires:    R-CRAN-paran 
Requires:         R-CRAN-OpenMx >= 2.19.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-R2HTML 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-psychTools 
Requires:         R-CRAN-paran 

%description
Quickly create, run, and report structural equation models, and twin
models. See '?umx' for help, and umx_open_CRAN_page("umx") for NEWS.
Timothy C. Bates, Michael C. Neale, Hermine H. Maes, (2019). umx: A
library for Structural Equation and Twin Modelling in R. Twin Research and
Human Genetics, 22, 27-41. <doi:10.1017/thg.2019.2>.

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
