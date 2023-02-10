%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kappalab
%global packver   0.4-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.10
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Additive Measure and Integral Manipulation Functions

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-kernlab 
Requires:         R-methods 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-kernlab 

%description
S4 tool box for capacity (or non-additive measure, fuzzy measure) and
integral manipulation in a finite setting. It contains routines for
handling various types of set functions such as games or capacities. It
can be used to compute several non-additive integrals: the Choquet
integral, the Sugeno integral, and the symmetric and asymmetric Choquet
integrals. An analysis of capacities in terms of decision behavior can be
performed through the computation of various indices such as the Shapley
value, the interaction index, the orness degree, etc. The well-known
M<f6>bius transform, as well as other equivalent representations of set
functions can also be computed. Kappalab further contains seven capacity
identification routines: three least squares based approaches, a method
based on linear programming, a maximum entropy like method based on
variance minimization, a minimum distance approach and an unsupervised
approach based on parametric entropies. The functions contained in
Kappalab can for instance be used in the framework of multicriteria
decision making or cooperative game theory.

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
