%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  randomForestVIP
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tune Random Forests Based on Variable Importance & Plot Results

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Functions for assessing variable relations and associations prior to
modeling with a Random Forest algorithm (although these are relevant for
any predictive model). Metrics such as partial correlations and variance
inflation factors are tabulated as well as plotted for the user. A
function is available for tuning the main Random Forest hyper-parameter
based on model performance and variable importance metrics. This
grid-search technique provides tables and plots showing the effect of the
main hyper-parameter on each of the assessment metrics. It also returns
each of the evaluated models to the user. The package also provides
superior variable importance plots for individual models. All of the plots
are developed so that the user has the ability to edit and improve further
upon the plots. Derivations and methodology are described in Bladen (2022)
<https://digitalcommons.usu.edu/etd/8587/>.

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
