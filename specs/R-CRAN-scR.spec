%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scR
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Sample Complexity Bounds

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-minpack.lm 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-progressr 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Provides tools for estimating empirical sample complexity bounds for
supervised learning tasks. The package supports simulation-based estimates
of generalization curves, parametric extrapolation of empirical sample
complexity bounds, theoretical bounds based on Vapnik-Chervonenkis
dimension, and optional monotone Gaussian process extrapolation for users
who install the external 'cmdstanr' workflow. For more details, see Carter
and Choi (2024) <doi:10.31219/osf.io/evrcj>.

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
