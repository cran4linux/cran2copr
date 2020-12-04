%global packname  SPOT
%global packver   2.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Parameter Optimization Toolbox

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-SimInf 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-smoof 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rsm 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-SimInf 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-smoof 

%description
A set of tools for model based optimization and tuning of algorithms. It
includes surrogate models, optimizers, and design of experiment
approaches. The main interface is spot, which uses sequentially updated
surrogate models for the purpose of efficient optimization. The main goal
is to ease the burden of objective function evaluations, when a single
evaluation requires a significant amount of resources.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
