%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitlandr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Vector Fields and Potential Landscapes from Intensive Longitudinal Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-simlandr >= 0.3.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-SparseVFC 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-simlandr >= 0.3.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-SparseVFC 
Requires:         R-CRAN-tidyr 

%description
A toolbox for estimating vector fields from intensive longitudinal data,
and construct potential landscapes thereafter. The vector fields can be
estimated with two nonparametric methods: the Multivariate Vector Field
Kernel Estimator (MVKE) by Bandi & Moloche (2018)
<doi:10.1017/S0266466617000305> and the Sparse Vector Field Consensus
(SparseVFC) algorithm by Ma et al.  (2013)
<doi:10.1016/j.patcog.2013.05.017>. The potential landscapes can be
constructed with a simulation-based approach with the 'simlandr' package
(Cui et al., 2021) <doi:10.31234/osf.io/pzva3>, or the Bhattacharya et al.
(2011) method for path integration <doi:10.1186/1752-0509-5-85>.

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
