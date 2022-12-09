%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  transform.hazards
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transforms Cumulative Hazards to Parameter Specified by ODE System

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Targets parameters that solve Ordinary Differential Equations (ODEs)
driven by a vector of cumulative hazard functions. The package provides a
method for estimating these parameters using an estimator defined by a
corresponding Stochastic Differential Equation (SDE) system driven by
cumulative hazard estimates. By providing cumulative hazard estimates as
input, the package gives estimates of the parameter as output, along with
pointwise (co)variances derived from an asymptotic expression. Examples of
parameters that can be targeted in this way include the survival function,
the restricted mean survival function, cumulative incidence functions,
among others; see Ryalen, Stensrud, and Røysland (2018)
<doi:10.1093/biomet/asy035>, and further applications in Stensrud,
Røysland, and Ryalen (2019) <doi:10.1111/biom.13102> and Ryalen et al.
(2021) <doi:10.1093/biostatistics/kxab009>.

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
