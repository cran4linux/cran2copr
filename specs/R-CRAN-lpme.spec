%global __brp_check_rpaths %{nil}
%global packname  lpme
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Estimation of Measurement Error Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.4.300.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-decon 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-locpol 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-decon 
Requires:         R-CRAN-flexmix 
Requires:         R-splines 
Requires:         R-CRAN-locpol 

%description
Provide nonparametric methods for mean regression model, modal regression
and conditional density estimation in the presence/absence of measurement
error. Bandwidth selection is also provided for each method. See Huang and
Zhou (2017) <doi:10.1080/10485252.2017.1303060>, Zhou and Huang (2016)
<doi:10.1214/16-EJS1210>, Huang and Zhou (2020) <doi:10.1214/20-EJS1688>,
and Zhou and Huang (2019) <doi:10.1080/03610918.2017.1402044>.

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
