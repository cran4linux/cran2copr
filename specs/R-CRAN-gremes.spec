%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gremes
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Tail Dependence in Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog >= 1.5.5
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-mev >= 1.13
BuildRequires:    R-CRAN-mvtnorm >= 1.0.8
BuildRequires:    R-CRAN-copula >= 0.999.19
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
Requires:         R-CRAN-quadprog >= 1.5.5
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-mev >= 1.13
Requires:         R-CRAN-mvtnorm >= 1.0.8
Requires:         R-CRAN-copula >= 0.999.19
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Provides tools for estimation of edge weights on graphical models with
respect to trees and block graphs and parameterized by a particular family
of max-stable copulas. The edge weights are parameters of tail dependence
between adjacent variables and these edge weights determine the joint tail
dependence between all variables in the context of a particular parametric
model. For methods of moment estimator, composite likelihood estimator
please see Asenova et al. (2021) <doi:10.1007/s10687-021-00407-5>. For
estimation based on extremal coefficients see Asenova et al. (2021) as
well as Einmahl et al. (2016) <doi:10.2139/ssrn.2717531>. For cliquewise
estimation please see Engelke and Hitz (2020) <doi:10.1111/rssb.12355>.

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
