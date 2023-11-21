%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shortIRT
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Procedures Based on Item Response Theory Models for the Development of Short Test Forms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TAM 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-TAM 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 

%description
Implement different Item Response Theory (IRT) based procedures for the
development of static short test forms (STFs) from a test. Two main
procedures are considered, specifically the typical IRT-based procedure
for the development of STF, and a recently introduced procedure (Epifania,
Anselmi & Robusto, 2022 <doi:10.1007/978-3-031-27781-8_7>). The procedures
differ in how the most informative items are selected for the inclusion in
the STF, either by considering their item information functions without
considering any specific level of the latent trait (typical procedure) or
by considering their informativeness with respect to specific levels of
the latent trait, denoted as theta targets (the newly introduced
procedure). Regarding the latter procedure, three methods are implemented
for the definition of the theta targets: (i) theta targets are defined by
segmenting the latent trait in equal intervals and considering the
midpoint of each interval (equal interval procedure, eip), (ii) by
clustering the latent trait to obtain unequal intervals and considering
the centroids of the clusters as the theta targets (unequal intervals
procedure, uip), and (iii) by letting the user set the specific theta
targets of interest (user-defined procedure, udp). For further details on
the procedure, please refer to Epifania, Anselmi & Robusto (2022)
<doi:10.1007/978-3-031-27781-8_7>.

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
