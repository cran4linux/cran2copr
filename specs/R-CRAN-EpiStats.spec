%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiStats
%global packver   1.6-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Epidemiologists

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-epiR 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-epiR 
Requires:         R-CRAN-dplyr 

%description
Provides set of functions aimed at epidemiologists. The package includes
commands for measures of association and impact for case control studies
and cohort studies. It may be particularly useful for outbreak
investigations including univariable analysis and stratified analysis. The
functions for cohort studies include the CS(), CSTable() and CSInter()
commands. The functions for case control studies include the CC(),
CCTable() and CCInter() commands. References - Cornfield, J. 1956. A
statistical problem arising from retrospective studies. In Vol. 4 of
Proceedings of the Third Berkeley Symposium, ed. J. Neyman, 135-148.
Berkeley, CA - University of California Press. Woolf, B. 1955. On
estimating the relation between blood group disease. Annals of Human
Genetics 19 251-253. Reprinted in Evolution of Epidemiologic Ideas
Annotated Readings on Concepts and Methods, ed. S. Greenland, pp. 108-110.
Newton Lower Falls, MA Epidemiology Resources. Gilles Desve & Peter
Makary, 2007. 'CSTABLE Stata module to calculate summary table for cohort
study' Statistical Software Components S456879, Boston College Department
of Economics. Gilles Desve & Peter Makary, 2007. 'CCTABLE Stata module to
calculate summary table for case-control study' Statistical Software
Components S456878, Boston College Department of Economics.

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
