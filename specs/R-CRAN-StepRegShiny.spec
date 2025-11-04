%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StepRegShiny
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical User Interface for 'StepReg'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-StepReg 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-summarytools 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-StepReg 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-summarytools 
Requires:         R-CRAN-rmarkdown 

%description
A web-based 'shiny' interface for the 'StepReg' package enables stepwise
regression analysis across linear, generalized linear (including logistic,
Poisson, Gamma, and negative binomial), and Cox models. It supports
forward, backward, bidirectional, and best-subset selection under a range
of criteria. The package also supports stepwise regression to multivariate
settings, allowing multiple dependent variables to be modeled
simultaneously. Users can explore and combine multiple selection
strategies and criteria to optimize model selection. For enhanced
robustness, the package offers optional randomized forward selection to
reduce overfitting, and a data-splitting workflow for more reliable
post-selection inference. Additional features include logging and
visualization of the selection process, as well as the ability to export
results in common formats.

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
