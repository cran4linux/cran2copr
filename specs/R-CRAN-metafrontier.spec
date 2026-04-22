%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metafrontier
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Metafrontier Models for Efficiency and Productivity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-methods 

%description
Implements metafrontier production function models for estimating
technical efficiencies and technology gaps for firms operating under
different technologies. Supports both stochastic frontier analysis (SFA)
and data envelopment analysis (DEA) based metafrontiers. Includes the
deterministic metafrontier of Battese, Rao, and O'Donnell (2004)
<doi:10.1023/B:PROD.0000012454.06094.29>, the stochastic metafrontier of
Huang, Huang, and Liu (2014) <doi:10.1007/s11123-014-0402-2>, and the
metafrontier Malmquist productivity index of O'Donnell, Rao, and Battese
(2008) <doi:10.1007/s00181-007-0119-4>. Additional features include panel
SFA with time-varying inefficiency, bootstrap confidence intervals for
technology gap ratios, latent class metafrontier estimation via the EM
algorithm, Murphy-Topel corrected standard errors, and 'ggplot2'
visualisation methods.

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
