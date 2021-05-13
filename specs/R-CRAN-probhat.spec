%global packname  probhat
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Generalized Kernel Smoothing and Related Statistical Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-barsurf 
BuildRequires:    R-CRAN-kubik 
Requires:         R-methods 
Requires:         R-CRAN-barsurf 
Requires:         R-CRAN-kubik 

%description
Probability mass functions (PMFs), probability density functions (PDFs),
cumulative distribution functions (CDFs) and quantile functions, mainly
via (optionally bounded/truncated) kernel smoothing. In the continuous
case, there's support for univariate, multivariate and conditional
distributions, including distributions that are both multivariate and
conditional. Refer to the book "Kernel Smoothing" by Wand and Jones
(1995), whose methods are generalized by the methods here. Also, supports
categorical distributions, mixed conditional distributions (with mixed
input types) and smooth empirical-like distributions, some of which, can
be used for statistical classification. There are extensions for computing
distance matrices (between distributions), multivariate probabilities,
multivariate random numbers, moment-based statistics and mode estimates.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
