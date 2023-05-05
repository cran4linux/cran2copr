%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  saccadr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Saccades via an Ensemble of Methods Approach

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 

%description
A modular and extendable approach to extract (micro)saccades from gaze
samples via an ensemble of methods. Although there is an agreement about a
general definition of a saccade, the more specific details are harder to
agree upon. Therefore, there are numerous algorithms that extract saccades
based on various heuristics, which differ in the assumptions about
velocity, acceleration, etc. The package uses three methods (Engbert and
Kliegl (2003) <doi:10.1016/S0042-6989(03)00084-1>, Otero-Millan et al.
(2014)<doi:10.1167/14.2.18>, and Nyström and Holmqvist (2010)
<doi:10.3758/BRM.42.1.188>) to label individual samples and then applies a
majority vote approach to identify saccades. The package includes three
methods but can be extended via custom functions. It also uses a modular
approach to compute velocity and acceleration from noisy samples. Finally,
you can obtain methods votes per gaze sample instead of saccades.

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
