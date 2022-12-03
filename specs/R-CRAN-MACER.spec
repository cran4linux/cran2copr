%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MACER
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Molecular Acquisition, Cleaning, and Evaluation in R 'MACER'

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rentrez 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-rentrez 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-httr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-grDevices 
Requires:         R-CRAN-png 

%description
To assist biological researchers in assembling taxonomically and marker
focused molecular sequence data sets. 'MACER' accepts a list of genera as
a user input and uses NCBI-GenBank and BOLD as resources to download and
assemble molecular sequence datasets. These datasets are then assembled by
marker, aligned, trimmed, and cleaned. The use of this package allows the
publication of specific parameters to ensure reproducibility. The 'MACER'
package has four core functions and an example run through using all of
these functions can be found in the associated repository
<https://github.com/rgyoung6/MACER_example>.

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
