%global __brp_check_rpaths %{nil}
%global packname  analytics
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Outlier Detection, Stationary Bootstrap, Testing WeakStationarity, NA Imputation, and Other Tools for Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-CRAN-VIM >= 4.7.0
BuildRequires:    R-tcltk >= 3.3.1
BuildRequires:    R-CRAN-powerplus >= 3.1
BuildRequires:    R-CRAN-car >= 2.1.4
BuildRequires:    R-cluster >= 2.0.4
BuildRequires:    R-CRAN-fractal >= 2.0.1
BuildRequires:    R-CRAN-urca >= 1.3.0
BuildRequires:    R-CRAN-TSA >= 1.01
BuildRequires:    R-CRAN-lmtest >= 0.9.35
BuildRequires:    R-CRAN-np >= 0.60.3
BuildRequires:    R-CRAN-robust >= 0.4.18
BuildRequires:    R-CRAN-trend >= 0.2.0
Requires:         R-MASS >= 7.3.45
Requires:         R-CRAN-VIM >= 4.7.0
Requires:         R-tcltk >= 3.3.1
Requires:         R-CRAN-powerplus >= 3.1
Requires:         R-CRAN-car >= 2.1.4
Requires:         R-cluster >= 2.0.4
Requires:         R-CRAN-fractal >= 2.0.1
Requires:         R-CRAN-urca >= 1.3.0
Requires:         R-CRAN-TSA >= 1.01
Requires:         R-CRAN-lmtest >= 0.9.35
Requires:         R-CRAN-np >= 0.60.3
Requires:         R-CRAN-robust >= 0.4.18
Requires:         R-CRAN-trend >= 0.2.0

%description
Current version includes outlier detection in a fitted linear model,
stationary bootstrap using a truncated geometric distribution, a
comprehensive test for weak stationarity, missing value imputation,
column/rows sums/means by group, weighted biplots, and a heuristic to
obtain a better initial configuration in non-metric MDS.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
