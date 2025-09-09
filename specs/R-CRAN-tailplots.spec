%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tailplots
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimators and Plots for Gamma and Pareto Tail Detection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Estimators for two functionals used to detect Gamma, Pareto or Lognormal
distributions, as well as distributions exhibiting similar tail behavior,
as introduced by Iwashita and Klar (2023) <doi:10.1111/stan.12316> and
Klar (2024) <doi:10.1080/00031305.2024.2413081>. One of these functionals,
g, originally proposed by Asmussen and Lehtomaa (2017)
<doi:10.3390/risks5010010>, distinguishes between log-convex and
log-concave tail behavior. Furthermore the characterization of the
lognormal distribution is based on the work of Mosimann (1970)
<doi:10.2307/2284599>. The package also includes methods for visualizing
these estimators and their associated confidence intervals across various
threshold values.

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
