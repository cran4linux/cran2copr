%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  facmodTS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Factor Models for Asset Returns

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-PortfolioAnalytics 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-RobStatTM 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-PortfolioAnalytics 
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-corpcor 
Requires:         R-methods 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-RobStatTM 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Supports teaching methods of estimating and testing time series factor
models for use in robust portfolio construction and analysis. Unique in
providing not only classical least squares, but also modern robust model
fitting methods which are not much influenced by outliers. Includes
returns and risk decompositions, with user choice of standard deviation,
value-at-risk, and expected shortfall risk measures. "Robust Statistics
Theory and Methods (with R)", R. A. Maronna, R. D. Martin, V. J. Yohai, M.
Salibian-Barrera (2019) <doi:10.1002/9781119214656>.

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
