%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SmokingHistoryGenerator
%global packver   6.5.3-1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.5.3.1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Package for the Smoking History Generator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-methods 
Requires:         R-CRAN-yaml 

%description
Efficient R interface to the Cancer Intervention and Surveillance Modeling
Network (CISNET) Smoking History Generator microsimulation engine, which
synthesizes individual smoking histories (initiation, cessation,
intensity) and ages at death from calibrated initiation, cessation,
cigarettes-per-day, and mortality tables. The wrapper exposes fixed-cohort
and population data-frame simulation, multi-threaded segmentation,
reproducible pseudo-random streams (L'Ecuyer RngStream MRG32k3a or
Matsumoto--Nishimura Mersenne Twister), legacy CLI-style configuration
files, and portable YAML configuration save/load with optional split
smoking and mortality parameter bundles. Methods follow Jeon et al. (2012)
<doi:10.1111/j.1539-6924.2011.01775.x>. Random number generators:
Matsumoto and Nishimura (1998) <doi:10.1145/272991.272995>; L'Ecuyer
(1999) <doi:10.1287/opre.47.1.159>; L'Ecuyer et al. (2002)
<doi:10.1287/opre.50.6.1073.358>.

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
