%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  semidist
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Measure Dependence Between Categorical and Continuous Variables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Semi-distance and mean-variance (MV) index are proposed to measure the
dependence between a categorical random variable and a continuous
variable. Test of independence and feature screening for classification
problems can be implemented via the two dependence measures. For the
details of the methods, see Zhong et al. (2023)
<doi:10.1080/01621459.2023.2284988>; Cui and Zhong (2019)
<doi:10.1016/j.csda.2019.05.004>; Cui, Li and Zhong (2015)
<doi:10.1080/01621459.2014.920256>.

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
