%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  varrank
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Heuristics Tools Based on Mutual Information for Variable Ranking

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-FNN 
Requires:         R-grDevices 

%description
A computational toolbox of heuristics approaches for performing variable
ranking and feature selection based on mutual information well adapted for
multivariate system epidemiology datasets. The core function is a general
implementation of the minimum redundancy maximum relevance model. R.
Battiti (1994) <doi:10.1109/72.298224>. Continuous variables are
discretized using a large choice of rule. Variables ranking can be learned
with a sequential forward/backward search algorithm. The two main problems
that can be addressed by this package is the selection of the most
representative variable within a group of variables of interest (i.e.
dimension reduction) and variable ranking with respect to a set of
features of interest.

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
