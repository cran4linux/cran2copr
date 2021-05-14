%global packname  cdmTools
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Useful Tools for Cognitive Diagnosis Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sirt >= 3.9.4
BuildRequires:    R-parallel >= 3.6.3
BuildRequires:    R-stats >= 3.6.3
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-GPArotation >= 2014.11.1
BuildRequires:    R-CRAN-GDINA >= 2.8.0
BuildRequires:    R-CRAN-psych >= 1.9.12
BuildRequires:    R-CRAN-combinat >= 0.0.8
Requires:         R-CRAN-sirt >= 3.9.4
Requires:         R-parallel >= 3.6.3
Requires:         R-stats >= 3.6.3
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-GPArotation >= 2014.11.1
Requires:         R-CRAN-GDINA >= 2.8.0
Requires:         R-CRAN-psych >= 1.9.12
Requires:         R-CRAN-combinat >= 0.0.8

%description
Provides useful tools for cognitive diagnosis modeling (CDM). The packages
includes the discrete factor loading method for Q-matrix estimation (Wang,
Song, & Ding, 2018, <doi:10.1007/978-3-319-77249-3_29>) and the Hull
method for Q-matrix validation (Nájera, Sorrel, de la Torre, & Abad, 2021,
<doi:10.1111/bmsp.12228>). It also provides dimensionality assessment
procedures for determining the number of attributes underlying CDM data,
including parallel analysis and automated CDM fit comparison as explored
in Nájera, Abad, and Sorrel (2021, <doi:10.3389/fpsyg.2021.614470>).
Lastly, the package provides some useful functions for CDM simulation
studies, such as random Q-matrix generation and detection of
complete/identified Q-matrices.

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
