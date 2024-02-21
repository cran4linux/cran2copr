%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lphom
%global packver   0.3.5-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Inference by Linear Programming under Homogeneity

License:          EPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-stats 
Requires:         R-CRAN-lpSolve 

%description
Provides a bunch of algorithms based on linear programming for estimating,
under the homogeneity hypothesis, RxC ecological contingency tables (or
vote transition matrices) using mainly aggregate data (from voting units).
References: Pavía and Romero (2022) <doi:10.1177/00491241221092725>. Pavía
(2023) <doi:10.1007/s43545-023-00658-y>. Pavía and Romero (2024)
<doi:10.1093/jrsssa/qnae013>. Pavía (2024) A local convergent ecological
inference algorithm for RxC tables. Pavía and Penadés (2024). A bottom-up
approach for ecological inference. Romero, Pavía, Martín and Romero (2020)
<doi:10.1080/02664763.2020.1804842>. Acknowledgements: The authors wish to
thank Consellería de Educación, Universidades y Empleo, Generalitat
Valenciana (grant AICO/2021/257) and Ministerio de Economía e Innovación
(grant PID2021-128228NB-I00) for supporting this research.

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
