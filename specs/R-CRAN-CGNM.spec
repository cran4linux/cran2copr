%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CGNM
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Gauss-Newton Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-shiny 

%description
Find multiple solutions of a nonlinear least squares problem.  Cluster
Gauss-Newton method does not assume uniqueness of the solution of the
nonlinear least squares problem and compute multiple minimizers. Please
cite the following paper when this software is used in your research: Aoki
et al. (2020) <doi:10.1007/s11081-020-09571-2>. Cluster Gauss–Newton
method. Optimization and Engineering, 1-31.  Please cite the following
paper when profile likelihood plot is drawn with this software and used in
your research: Aoki and Sugiyama (2024) <doi:10.1002/psp4.13055>. Cluster
Gauss-Newton method for a quick approximation of profile likelihood: With
application to physiologically-based pharmacokinetic models. CPT
Pharmacometrics Syst Pharmacol.13(1):54-67.

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
