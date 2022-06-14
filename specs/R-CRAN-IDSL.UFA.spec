%global __brp_check_rpaths %{nil}
%global packname  IDSL.UFA
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          United Formula Annotation (UFA) for HRMS Data Processing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-IDSL.IPA >= 1.7
BuildRequires:    R-CRAN-IDSL.MXP >= 1.4
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-IDSL.IPA >= 1.7
Requires:         R-CRAN-IDSL.MXP >= 1.4
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-RNetCDF 
Requires:         R-CRAN-base64enc 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-CRAN-readxl 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
A pipeline to annotate peaklists from the IDSL.IPA package with molecular
formula using an isotopic profile matching approach. The IDSL.UFA pipeline
is especially beneficial when MS/MS data are not available. The IDSL.UFA
package has functions to process user-defined adduct formulas.

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
