%global __brp_check_rpaths %{nil}
%global packname  albatross
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          PARAFAC Analysis of Fluorescence Excitation-Emission Matrices

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-multiway >= 1.0.4
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-multiway >= 1.0.4
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-lattice 
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 

%description
Perform parallel factor analysis (PARAFAC: Hitchcock, 1927)
<doi:10.1002/sapm192761164> on fluorescence excitation-emission matrices
(FEEMs): handle scattering signal and inner filter effect, scale the
dataset, fit the model; perform split-half validation or jack-knifing. A
modified approach called "randomised split-half" is also available. The
package has a low dependency footprint (only two direct dependencies not
in core or recommended; four total non-core/recommended dependencies) and
has been tested on a wide range of R versions (including R as old as 3.3.3
from Debian Stretch).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
