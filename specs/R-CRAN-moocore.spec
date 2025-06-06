%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  moocore
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Core Mathematical Functions for Multi-Objective Optimization

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Rdpack 

%description
Fast implementation of mathematical operations and performance metrics for
multi-objective optimization, including filtering and ranking of dominated
vectors according to Pareto optimality, computation of the empirical
attainment function, V.G. da Fonseca, C.M. Fonseca, A.O. Hall (2001)
<doi:10.1007/3-540-44719-9_15>, hypervolume metric, C.M. Fonseca, L.
Paquete, M. López-Ibáñez (2006) <doi:10.1109/CEC.2006.1688440>, epsilon
indicator, inverted generational distance, and Vorob'ev threshold,
expectation and deviation, M. Binois, D. Ginsbourger, O. Roustant (2015)
<doi:10.1016/j.ejor.2014.07.032>, among others.

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
