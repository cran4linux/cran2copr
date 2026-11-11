%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  r2sbml
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Read 'SBML' Models and Convert Them to Simulation Code

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-Rcpp >= 0.12.6

%description
Reads models in the Systems Biology Markup Language ('SBML') (Hucka et al.
(2003) <doi:10.1093/bioinformatics/btg015>) through the bundled 'libSBML'
library (Bornstein et al. (2008) <doi:10.1093/bioinformatics/btn051>).
Lists a model's species, parameters, compartments, reactions, rules,
events and function definitions, and converts the model into ready-to-run
simulation code for 'deSolve', 'mrgsolve', 'rxode2', 'MATLAB', 'Julia' or
'ubiquity'. Models are read, not modified.

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
