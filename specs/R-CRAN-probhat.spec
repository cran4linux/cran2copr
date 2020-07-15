%global packname  probhat
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Multivariate Generalized Kernel Smoothing and RelatedStatistical Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intoo 
BuildRequires:    R-CRAN-barsurf 
BuildRequires:    R-CRAN-kubik 
Requires:         R-CRAN-intoo 
Requires:         R-CRAN-barsurf 
Requires:         R-CRAN-kubik 

%description
Mass functions, density functions, distribution functions and quantile
functions via continuous kernel smoothing, and to a lesser extent,
discrete kernel smoothing. Also, supports categorical distributions and
smooth empirical-like distributions. There are univariate, multivariate
and conditional distributions, including multivariate-conditional
distributions and conditional distributions with mixed input types, along
with functions for plotting univariate, bivariate and trivariate
distributions. Conditional categorical distributions with mixed input
types can be used for statistical classification purposes. And there are
extensions for computing multivariate probabilities, multivariate random
numbers, moment-based statistics, robust-based statistics and mode
estimates.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
