%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  investlabr
%global packver   0.0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Research Workflows for Macro and Cross-Asset Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-ggrepel 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-Rcpp 

%description
Reusable research workflows for macro-financial and cross-asset analysis.
The package sits on top of data packages such as 'investdatar' and focuses
on transforming existing market and macro data into analysis-ready
research tables, factor and indicator constructions, event and regime
overlays, sensitivity estimates, scenario comparisons, and research-grade
visualization outputs. Portfolio risk-return comparisons use the
mean-variance framework of Markowitz (1952)
<doi:10.1111/j.1540-6261.1952.tb01525.x>. Research-side volatility
simulations include the generalized autoregressive conditional
heteroskedasticity model of Bollerslev (1986)
<doi:10.1016/0304-4076(86)90063-1>.

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
