%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbcc
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Risk-Based Control Charts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-PearsonDS 
BuildRequires:    R-CRAN-qcc 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-parallel 
Requires:         R-CRAN-PearsonDS 
Requires:         R-CRAN-qcc 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements univariate and multivariate risk-based control charts for
statistical process control in the presence of measurement uncertainty.
Available charts include Shewhart X-bar, R, and S charts, moving-average
charts, exponentially weighted moving-average charts, cumulative-sum
charts, and Hotelling T-squared charts. Chart parameters can be optimized
by minimizing the total cost of the four decision outcomes. The
methodology is described by Kosztyan and Katona (2016)
<doi:10.1016/j.eswa.2016.06.019>, Kosztyan and Katona (2018)
<doi:10.1016/j.cie.2018.04.052>, Katona et al. (2023)
<doi:10.1109/ACCESS.2023.3312226>, Saghir et al. (2025)
<doi:10.1016/j.rineng.2025.107278>, and Saghir et al. (2026)
<doi:10.1016/j.rico.2026.100661>.

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
