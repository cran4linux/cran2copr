%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  outliers.ts.oga
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Outlier Detection for Large Time Series Databases

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.22.0
BuildRequires:    R-CRAN-caret >= 6.0.94
BuildRequires:    R-CRAN-future >= 1.67.0
BuildRequires:    R-CRAN-parallelly >= 1.37.1
BuildRequires:    R-CRAN-future.apply >= 1.20.0
BuildRequires:    R-CRAN-robust >= 0.7.4
BuildRequires:    R-CRAN-gsarima >= 0.1.5
Requires:         R-CRAN-forecast >= 8.22.0
Requires:         R-CRAN-caret >= 6.0.94
Requires:         R-CRAN-future >= 1.67.0
Requires:         R-CRAN-parallelly >= 1.37.1
Requires:         R-CRAN-future.apply >= 1.20.0
Requires:         R-CRAN-robust >= 0.7.4
Requires:         R-CRAN-gsarima >= 0.1.5

%description
Programs for detecting and cleaning outliers in single time series and in
time series from homogeneous and heterogeneous databases using an
Orthogonal Greedy Algorithm (OGA) for saturated linear regression models.
The programs implement the procedures presented in the paper entitled
"Efficient Outlier Detection for Large Time Series Databases" by Pedro
Galeano, Daniel Peña and Ruey S. Tsay (2026), working paper, Universidad
Carlos III de Madrid. Version 1.1.2 fixes one bug.

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
