%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CamelRatiosIndex
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate-Weighted Indexing of CAMEL Ratios for Bank Performance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-robustfa 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-robustfa 
Requires:         R-CRAN-rrcov 
Requires:         R-stats 
Requires:         R-utils 

%description
Computes a composite year-on-year index for bank performance assessment
using the CAMEL framework (Capital Adequacy, Asset Quality, Management
Efficiency, Earnings, Liquidity). The multivariate weighting scheme
employs factor analysis with robust covariance estimation to derive
communality-based weights from the correlation matrix of CAMEL ratios.
Provides functions for index computation, visualization, and comparison
across banks and time periods.The methodology is described in Ayimah et
al. (2023a) <doi:10.9734/bpi/mono/978-81-19315-32-1> and Ayimah et al.
(2023b) <https://ajtem.com/index.php/ajtem/article/view/53>.

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
