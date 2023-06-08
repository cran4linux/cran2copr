%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpiceFP
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Method to Identify Joint Effects of Functional Predictors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-genlasso 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-genlasso 
Requires:         R-CRAN-purrr 

%description
A set of functions allowing to implement the 'SpiceFP' approach which is
iterative. It involves transformation of functional predictors into
several candidate explanatory matrices (based on contingency tables), to
which relative edge matrices with contiguity constraints are associated.
Generalized Fused Lasso regression are performed in order to identify the
best candidate matrix, the best class intervals and related coefficients
at each iteration. The approach is stopped when the maximal number of
iterations is reached or when retained coefficients are zeros.
Supplementary functions allow to get coefficients of any candidate matrix
or mean of coefficients of many candidates. The methods in this package
are describing in Girault Gnanguenon Guesse, Patrice Loisel, Bénedicte
Fontez, Thierry Simonneau, Nadine Hilgert (2021) "An exploratory penalized
regression to identify combined effects of functional variables
-Application to agri-environmental issues"
<https://hal.archives-ouvertes.fr/hal-03298977>.

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
