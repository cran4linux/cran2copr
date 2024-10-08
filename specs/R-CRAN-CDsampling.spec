%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CDsampling
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'CDsampling': Constraint Sampling in Paid Research Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-stats 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Rglpk 
Requires:         R-stats 

%description
In the context of paid research studies and clinical trials, budget
considerations and patient sampling from available populations are subject
to inherent constraints. We introduce the 'CDsampling' package, which
integrates optimal design theories within the framework of constrained
sampling. This package offers the possibility to find both D-optimal
approximate and exact allocations for samplings with or without
constraints. Additionally, it provides functions to find constrained
uniform sampling as a robust sampling strategy with limited model
information. Our package offers functions for the computation of the
Fisher information matrix under generalized linear models (including
regular linear regression model) and multinomial logistic models.To
demonstrate the applications, we also provide a simulated dataset and a
real dataset embedded in the package. Yifei Huang, Liping Tong, and Jie
Yang (2025)<doi:10.5705/ss.202022.0414>.

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
