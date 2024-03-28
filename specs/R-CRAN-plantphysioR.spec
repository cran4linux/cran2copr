%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plantphysioR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fundamental Formulas for Plant Physiology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Functions tailored for scientific and student communities involved in
plant science research. Functionalities encompass estimation chlorophyll
content according to Arnon (1949) <doi:10.1104/pp.24.1.1>, determination
water potential of Polyethylene glycol(PEG)6000 as in Michel and Kaufmann
(1973) <doi:10.1104/pp.51.5.914> and functions related to estimation of
yield related indices like Abiotic tolerance index as given by Moosavi et
al.(2008)<doi:10.22059/JDESERT.2008.27115>, Geometric mean productivity
(GMP) by Fernandez (1992) <ISBN:92-9058-081-X>, Golden Mean by Moradi et
al.(2012)<doi:10.14207/ejsd.2012.v1n3p543>, HAM by Schneider et
al.(1997)<doi:10.2135/cropsci1997.0011183X003700010007x>,MPI and TOL by
Hossain etal., (1990)<doi:10.2135/cropsci1990.0011183X003000030030x>, RDI
by Fischer et al. (1979)<doi:10.1071/AR9791001>,SSI by Fisher et
al.(1978)<doi:10.1071/AR9780897>, STI by Fernandez
(1993)<doi:10.22001/wvc.72511>,YSI by Bouslama & Schapaugh
(1984)<doi:10.2135/cropsci1984.0011183X002400050026x>, Yield index by
Gavuzzi et al.(1997)<doi:10.4141/P96-130>.

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
