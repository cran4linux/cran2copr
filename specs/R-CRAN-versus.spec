%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  versus
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Data Frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-collapse >= 2.0.9
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-vctrs >= 0.6.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-collapse >= 2.0.9
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-vctrs >= 0.6.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 

%description
A toolset for interactively exploring the differences between two data
frames.

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
