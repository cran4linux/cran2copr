%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ruin
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation of Various Risk Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-methods 
Requires:         R-parallel 

%description
A (not yet exhaustive) collection of common models of risk processes in
actuarial science, represented as formal S4 classes. Each class (risk
model) has a simulator of its path, and a plotting function. Further, a
Monte-Carlo estimator of a ruin probability for a finite time is
implemented, using a parallel computation. Currently, the package extends
two classical risk models Cramer-Lundberg and Sparre Andersen models by
including capital injections, that are positive jumps (see Breuer L. and
Badescu A.L. (2014) <doi:10.1080/03461238.2011.636969>). The intent of the
package is to provide a user-friendly interface for ruin processes'
simulators, as well as a solid and extensible structure for future
extensions.

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
