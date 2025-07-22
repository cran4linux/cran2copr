%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  paramlink
%global packver   1.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Linkage and Other Pedigree Analysis in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-graphics 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-maxLik 
Requires:         R-stats 
Requires:         R-utils 

%description
NOTE: 'PARAMLINK' HAS BEEN SUPERSEDED BY THE 'PEDSUITE' PACKAGES
(<https://magnusdv.github.io/pedsuite/>). 'PARAMLINK' IS MAINTAINED ONLY
FOR LEGACY PURPOSES AND SHOULD NOT BE USED IN NEW PROJECTS. A suite of
tools for analysing pedigrees with marker data, including parametric
linkage analysis, forensic computations, relatedness analysis and marker
simulations. The core of the package is an implementation of the
Elston-Stewart algorithm for pedigree likelihoods, extended to allow
mutations as well as complex inbreeding. Features for linkage analysis
include singlepoint LOD scores, power analysis, and multipoint analysis
(the latter through a wrapper to the 'MERLIN' software). Forensic
applications include exclusion probabilities, genotype distributions and
conditional simulations. Data from the 'Familias' software can be imported
and analysed in 'paramlink'. Finally, 'paramlink' offers many utility
functions for creating, manipulating and plotting pedigrees with or
without marker data (the actual plotting is done by the 'kinship2'
package).

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
