%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GENMETA
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implements Generalized Meta-Analysis Using Iterated Reweighted Least Squares Algorithm

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-pracma 

%description
Generalized meta-analysis is a technique for estimating parameters
associated with a multiple regression model through meta-analysis of
studies which may have information only on partial sets of the regressors.
It estimates the effects of each variable while fully adjusting for all
other variables that are measured in at least one of the studies. Using
algebraic relationships between regression parameters in different
dimensions, a set of moment equations is specified for estimating the
parameters of a maximal model through information available on sets of
parameter estimates from a series of reduced models available from the
different studies. The specification of the equations requires a reference
dataset to estimate the joint distribution of the covariates. These
equations are solved using the generalized method of moments approach,
with the optimal weighting of the equations taking into account
uncertainty associated with estimates of the parameters of the reduced
models. The proposed framework is implemented using iterated reweighted
least squares algorithm for fitting generalized linear regression models.
For more details about the method, please see pre-print version of the
manuscript on generalized meta-analysis by Prosenjit Kundu, Runlong Tang
and Nilanjan Chatterjee (2018) <doi:10.1093/biomet/asz030>.The current
version (0.2.0) is updated to address some of the stability issues in the
previous version (0.1).

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
