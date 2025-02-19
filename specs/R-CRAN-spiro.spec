%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spiro
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Manage Data from Cardiopulmonary Exercise Testing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-signal 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-signal 

%description
Import, process, summarize and visualize raw data from metabolic carts.
See Robergs, Dwyer, and Astorino (2010)
<doi:10.2165/11319670-000000000-00000> for more details on data
processing.

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
