%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DepCens
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dependent Censoring Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dlm 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-stats 
Requires:         R-CRAN-dlm 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-matrixStats 
Requires:         R-stats 

%description
Dependent censoring regression models for survival multivariate data.
These models are based on extensions of the frailty models, capable to
accommodating the dependence between failure and censoring times, with
Weibull and piecewise exponential marginal distributions. Theoretical
details regarding the models implemented in the package can be found in
Schneider et al. (2019) <doi:10.1002/bimj.201800391>.

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
