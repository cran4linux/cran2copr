%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DynNom
%global packver   5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualising Statistical Models using Dynamic Nomograms

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 > 2.1.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-stargazer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-compare 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-ggplot2 > 2.1.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-stargazer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-compare 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-survival 

%description
Demonstrate the results of a statistical model object as a dynamic
nomogram in an RStudio panel or web browser. The package provides two
generics functions: DynNom, which display statistical model objects as a
dynamic nomogram; DNbuilder, which builds required scripts to publish a
dynamic nomogram on a web server such as the <https://www.shinyapps.io/>.
Current version of 'DynNom' supports stats::lm, stats::glm,
survival::coxph, rms::ols, rms::Glm, rms::lrm, rms::cph, and mgcv::gam
model objects.

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
