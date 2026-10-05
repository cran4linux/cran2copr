%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mpindex
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Poverty Index (MPI) via the Alkire-Foster Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-tsg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-tsg 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 

%description
Estimate Multidimensional Poverty Index (MPI) measures from household
survey microdata using the Alkire-Foster dual-cutoff counting method
(Alkire and Foster, 2011). Load indicator specifications from CSV, Excel,
JSON, or plain-text files; compute the headcount ratio (H), intensity (A),
and MPI = H x A across any subgroup; and export results to formatted Excel
reports. Supports complex survey designs — stratification, clustering, and
probability weights — and optionally appends design-based standard errors
and confidence intervals.

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
