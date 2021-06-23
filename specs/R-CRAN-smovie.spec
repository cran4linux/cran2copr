%global __brp_check_rpaths %{nil}
%global packname  smovie
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Some Movies to Illustrate Concepts in Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel >= 1.1.3
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-rpanel >= 1.1.3
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides movies to help students to understand statistical concepts.  The
'rpanel' package <https://cran.r-project.org/package=rpanel> is used to
create interactive plots that move to illustrate key statistical ideas and
methods.  There are movies to: visualise probability distributions
(including user-supplied ones); illustrate sampling distributions of the
sample mean (central limit theorem), the median, the sample maximum
(extremal types theorem) and (the Fisher transformation of the) product
moment correlation coefficient; examine the influence of an individual
observation in simple linear regression; illustrate key concepts in
statistical hypothesis testing. Also provided are dpqr functions for the
distribution of the Fisher transformation of the correlation coefficient
under sampling from a bivariate normal distribution.

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
