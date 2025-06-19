%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wqc
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet Quantile Correlation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-QCSIS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-QCSIS 
Requires:         R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-grid 
Requires:         R-CRAN-viridisLite 

%description
Estimate and plot wavelet quantile correlations(Kumar and Padakandla,2022)
between two time series. Wavelet quantile correlation is used to capture
the dependency between two time series across quantiles and different
frequencies. This method is useful in identifying potential hedges and
safe-haven instruments for investment purposes. See Kumar and
Padakandla(2022) <doi:10.1016/j.frl.2022.102707> for further details.

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
