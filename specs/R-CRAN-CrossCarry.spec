%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CrossCarry
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Data from a Crossover Design with GEE

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gee 
Requires:         R-CRAN-ggplot2 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
Analyze data from a crossover design using generalized estimation
equations (GEE), including carryover effects and various correlation
structures based on the Kronecker product. It contains functions for
semiparametric estimates of carry-over effects in repeated measures and
allows estimation of complex carry-over effects. Related work includes: a)
Cruz N.A., Melo O.O., Martinez C.A. (2023). "CrossCarry: An R package for
the analysis of data from a crossover design with GEE".
<doi:10.48550/arXiv.2304.02440>. b) Cruz N.A., Melo O.O., Martinez C.A.
(2023). "A correlation structure for the analysis of Gaussian and
non-Gaussian responses in crossover experimental designs with repeated
measures". <doi:10.1007/s00362-022-01391-z> and c) Cruz N.A., Melo O.O.,
Martinez C.A. (2023). "Semiparametric generalized estimating equations for
repeated measurements in cross-over designs".
<doi:10.1177/09622802231158736>.

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
