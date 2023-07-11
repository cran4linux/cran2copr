%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  designmatch
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Matched Samples that are Balanced and Representative by Design

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-highs 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-highs 

%description
Includes functions for the construction of matched samples that are
balanced and representative by design.  Among others, these functions can
be used for matching in observational studies with treated and control
units, with cases and controls, in related settings with instrumental
variables, and in discontinuity designs.  Also, they can be used for the
design of randomized experiments, for example, for matching before
randomization.  By default, 'designmatch' uses the 'highs' optimization
solver, but its performance is greatly enhanced by the 'Gurobi'
optimization solver and its associated R interface.  For their
installation, please follow the instructions at
<https://www.gurobi.com/documentation/quickstart.html> and
<https://www.gurobi.com/documentation/7.0/refman/r_api_overview.html>.  We
have also included directions in the gurobi_installation file in the inst
folder.

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
