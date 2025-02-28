%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FBMS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Bayesian Model Selection and Model Averaging

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-fastglm 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-r2r 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-fastglm 
Requires:         R-CRAN-GenSA 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-r2r 
Requires:         R-CRAN-Rcpp 

%description
Implements the Mode Jumping Markov Chain Monte Carlo algorithm described
in <doi:10.1016/j.csda.2018.05.020> and its Genetically Modified
counterpart described in <doi:10.1613/jair.1.13047> as well as the
sub-sampling versions described in <doi:10.1016/j.ijar.2022.08.018> for
flexible Bayesian model selection and model averaging.

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
