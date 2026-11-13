%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MFO
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Maximal Fat Oxidation and Kinetics Calculation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tidyr 

%description
Computes the maximal fat oxidation (MFO), the exercise intensity that
elicits it (Fatmax), the Fatmax zone and the crossover point from indirect
calorimetry data of a graded exercise test. Substrate oxidation is
estimated with the stoichiometric equations of Frayn (1983)
<doi:10.1152/jappl.1983.55.2.628>, Peronnet and Massicotte (1991, Can J
Sport Sci 16(1):23-29) or Jeukendrup and Wallis (2005)
<doi:10.1055/s-2004-830512>, and Fatmax is located with a third- or
second-degree polynomial, the measured values or the MRER method. Fat
oxidation kinetics are described with the SIN model of Cheneviere et al.
(2009) <doi:10.1249/MSS.0b013e31819e2f91>, which returns dilatation,
symmetry and translation, together with the intensity at which fat
oxidation becomes negligible (Fatmin). Applications of these methods are
given in Achten et al. (2002) <doi:10.1097/00005768-200201000-00015> and
Montes de Oca et al. (2021) <doi:10.1080/17461391.2020.1788650>.

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
