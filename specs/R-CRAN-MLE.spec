%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLE
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Estimation of Various Univariate and Multivariate Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BGFD 
BuildRequires:    R-CRAN-bivpois 
BuildRequires:    R-CRAN-Compositional 
BuildRequires:    R-CRAN-Directional 
BuildRequires:    R-CRAN-geppe 
BuildRequires:    R-CRAN-gp 
BuildRequires:    R-CRAN-MN 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-skellam 
Requires:         R-CRAN-BGFD 
Requires:         R-CRAN-bivpois 
Requires:         R-CRAN-Compositional 
Requires:         R-CRAN-Directional 
Requires:         R-CRAN-geppe 
Requires:         R-CRAN-gp 
Requires:         R-CRAN-MN 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-skellam 

%description
Several functions for maximum likelihood estimation of various univariate
and multivariate distributions. The list includes more than 100 univariate
continuous and discrete distributions, distributions that lie on the real
line, the positive line, interval restricted, circular distributions.
Further, multivariate continuous and discrete distributions, distributions
for compositional and directional data, etc. Some references include
Johnson N. L., Kotz S. and Balakrishnan N. (1994). "Continuous Univariate
Distributions, Volume 1" <ISBN:978-0-471-58495-7>, Johnson, Norman L.
Kemp, Adrianne W. Kotz, Samuel (2005). "Univariate Discrete
Distributions". <ISBN:978-0-471-71580-1> and Mardia, K. V. and Jupp, P. E.
(2000). "Directional Statistics". <ISBN:978-0-471-95333-3>.

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
