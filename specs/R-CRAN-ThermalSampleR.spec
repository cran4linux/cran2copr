%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ThermalSampleR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Sample Sizes Required for Critical Thermal Limits Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-base >= 3.4.0
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-stats >= 3.4.0
Requires:         R-graphics >= 3.4.0
Requires:         R-base >= 3.4.0
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-testthat 

%description
We present a range of simulations to aid researchers in determining
appropriate sample sizes when performing critical thermal limits studies
(e.g. CTmin/CTmin experiments). A number of wrapper functions are provided
for plotting and summarising outputs from these simulations. These
simulations are presented in van Steenderen, C.J.M., Sutton, G.F., Owen,
C.A., Martin, G.D., and Coetzee, J.A. Sample size assessments for thermal
physiology studies: An R package and R Shiny GUI. 2023. Physiological
Entomology. Under review. The GUI version of this package is available on
the R Shiny online server at:
<https://clarkevansteenderen.shinyapps.io/ThermalSampleR_Shiny/> , or it
is accessible via GitHub at
<https://github.com/clarkevansteenderen/ThermalSampleR_Shiny/>. We would
like to thank Grant Duffy (University of Otago, Dundedin, New Zealand) for
granting us permission to use the source code for the Test of Total
Equivalency function.

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
