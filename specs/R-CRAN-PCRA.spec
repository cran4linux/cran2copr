%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PCRA
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Companion to Portfolio Construction and Risk Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-PortfolioAnalytics 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-RobStatTM 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-R.cache 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-PortfolioAnalytics 
Requires:         R-CRAN-boot 
Requires:         R-methods 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-RobStatTM 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-R.cache 

%description
A collection of functions and data sets that support teaching a
quantitative finance MS level course on Portfolio Construction and Risk
Analysis, and the writing of a textbook for such a course.  The package is
unique in providing several real-world data sets that may be used for
problem assignments and student projects.  The data sets include
cross-sections of stock data from the Center for Research on Security
Prices, LLC (CRSP), corresponding factor exposures data from S&P Global,
and several SP500 data sets.

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
