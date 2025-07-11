%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesMortalityPlus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Mortality Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mvtnorm 

%description
Fit Bayesian graduation mortality using the Heligman-Pollard model, as
seen in Heligman, L., & Pollard, J. H. (1980)
<doi:10.1017/S0020268100040257> and Dellaportas, Petros, et al. (2001)
<doi:10.1111/1467-985X.00202>, and dynamic linear model (Campagnoli, P.,
Petris, G., and Petrone, S. (2009) <doi:10.1007/b135794_2>). While
Heligman-Pollard has parameters with a straightforward interpretation
yielding some rich analysis, the dynamic linear model provides a very
flexible adjustment of the mortality curves by controlling the discount
factor value. Closing methods for both Heligman-Pollard and dynamic linear
model were also implemented according to Dodd, Erengul, et al. (2018)
<https://www.jstor.org/stable/48547511>. The Bayesian Lee-Carter model is
also implemented to fit historical mortality tables time series to predict
the mortality in the following years and to do improvement analysis, as
seen in Lee, R. D., & Carter, L. R. (1992)
<doi:10.1080/01621459.1992.10475265> and Pedroza, C. (2006)
<doi:10.1093/biostatistics/kxj024>. Journal publication available at
<doi:10.18637/jss.v113.i09>.

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
