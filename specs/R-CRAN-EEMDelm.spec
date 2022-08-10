%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EEMDelm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble Empirical Mode Decomposition and Its Variant Based ELM Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-nnfor 
BuildRequires:    R-CRAN-Rlibeemd 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-nnfor 
Requires:         R-CRAN-Rlibeemd 

%description
Forecasting univariate time series with different decomposition based
Extreme Learning Machine models. For method details see Yu L, Wang S, Lai
KK (2008). <doi:10.1016/j.eneco.2008.05.003>, Parida M, Behera MK, Nayak N
(2018). <doi:10.1109/ICSESP.2018.8376723>.

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
