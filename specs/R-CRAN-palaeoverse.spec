%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  palaeoverse
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Prepare and Explore Data for Palaeobiological Analyses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-h3jsr >= 1.3.0
BuildRequires:    R-CRAN-deeptime >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-h3jsr >= 1.3.0
Requires:         R-CRAN-deeptime >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-pbapply 

%description
Provides functionality to support data preparation and exploration for
palaeobiological analyses, improving code reproducibility and
accessibility. The wider aim of 'palaeoverse' is to bring the
palaeobiological community together to establish agreed standards. The
package currently includes functionality for data cleaning, binning (time
and space), exploration, summarisation and visualisation. Reference
datasets (i.e. Geological Time Scales <https://stratigraphy.org/chart>)
and auxiliary functions are also provided. Details can be found in: Jones
et al., (2022) <doi:10.31223/X5Z94Q>.

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
