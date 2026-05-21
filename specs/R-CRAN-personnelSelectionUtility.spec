%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  personnelSelectionUtility
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Analysis Methods for Personnel Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Implements classical and contemporary utility-analysis methods for
personnel selection, organised by criterion scale (classification or
continuous/monetary) and selection structure (compensatory or
multiple-hurdle). Methods include Taylor-Russell classification (Taylor
and Russell, 1939, <doi:10.1037/h0057079>), Brogden-Cronbach-Gleser
monetary utility (Brogden, 1949,
<doi:10.1111/j.1744-6570.1949.tb01397.x>), Schmidt-Hunter-Pearlman
intervention utility (Schmidt and others, 1979,
<doi:10.1037/0021-9010.64.6.609>), Sturman comprehensive cascade (Sturman,
2001, <doi:10.1108/eb029072>), Thomas-Owen-Gunst multivariate
classification (Thomas and others, 1977, <doi:10.3102/10769986002001055>),
compensatory versus multiple-hurdle simulation (Ock and Oswald, 2018,
<doi:10.1027/1866-5888/a000205>), AUC-to-effect-size conversions (Salgado,
2018, <doi:10.5093/ejpalc2018a5>), Pareto frontiers for validity-diversity
trade-offs, and Monte Carlo uncertainty propagation.

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
