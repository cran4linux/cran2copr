%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nbconv
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluate Arbitrary Negative Binomial Convolutions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-matrixStats 
Requires:         R-stats 

%description
Three distinct methods are implemented for evaluating the sums of
arbitrary negative binomial distributions. These methods are: Furman's
exact probability mass function (Furman (2007)
<doi:10.1016/j.spl.2006.06.007>), saddlepoint approximation, and a method
of moments approximation. Functions are provided to calculate the density
function, the distribution function and the quantile function of the
convolutions in question given said evaluation methods. Functions for
generating random deviates from negative binomial convolutions and for
directly calculating the mean, variance, skewness, and excess kurtosis of
said convolutions are also provided.

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
