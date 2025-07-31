%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PAGE
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predictor-Assisted Graphical Models under Error-in-Variables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-metrica 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-network 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-metrica 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-RSQLite 

%description
We consider the network structure detection for variables Y with auxiliary
variables X accommodated, which are possibly subject to measurement error.
The following three functions are designed to address various structures
by different methods : one is NP_Graph() that is used for handling the
nonlinear relationship between the responses and the covariates, another
is Joint_Gaussian() that is used for correction in linear regression
models via the Gaussian maximum likelihood, and the other Cond_Gaussian()
is for linear regression models via conditional likelihood function.

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
