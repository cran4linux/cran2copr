%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPGame
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Solving Complex Game Problems using Gaussian Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-GPareto 
BuildRequires:    R-CRAN-KrigInv 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-GPareto 
Requires:         R-CRAN-KrigInv 
Requires:         R-CRAN-DiceDesign 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-CRAN-matrixStats 

%description
Sequential strategies for finding a game equilibrium are proposed in a
black-box setting (expensive pay-off evaluations, no derivatives). The
algorithm handles noiseless or noisy evaluations. Two acquisition
functions are available. Graphical outputs can be generated automatically.
V. Picheny, M. Binois, A. Habbal (2018) <doi:10.1007/s10898-018-0688-0>.
M. Binois, V. Picheny, P. Taillandier, A. Habbal (2020)
<doi:10.48550/arXiv.1902.06565>.

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
