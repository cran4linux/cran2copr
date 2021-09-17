%global __brp_check_rpaths %{nil}
%global packname  fsr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Handling Fuzzy Spatial Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-utils >= 3.6.3
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-FuzzyR >= 2.3.0
BuildRequires:    R-methods >= 2.0.0
BuildRequires:    R-CRAN-e1071 >= 1.7.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-pso >= 1.0.3
BuildRequires:    R-CRAN-sf >= 0.9.4
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-lwgeom >= 0.2.6
Requires:         R-utils >= 3.6.3
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-FuzzyR >= 2.3.0
Requires:         R-methods >= 2.0.0
Requires:         R-CRAN-e1071 >= 1.7.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-pso >= 1.0.3
Requires:         R-CRAN-sf >= 0.9.4
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-lwgeom >= 0.2.6

%description
Support for fuzzy spatial objects, their operations, and fuzzy spatial
inference models based on Spatial Plateau Algebra. It employs fuzzy set
theory and fuzzy logic as foundation to deal with spatial fuzziness. It
implements underlying concepts defined in the following research papers:
(i) "Spatial Plateau Algebra: An Executable Type System for Fuzzy Spatial
Data Types" <doi:10.1109/FUZZ-IEEE.2018.8491565>; (ii) "A Systematic
Approach to Creating Fuzzy Region Objects from Real Spatial Data Sets"
<doi:10.1109/FUZZ-IEEE.2019.8858878>; (iii) "Fuzzy Inference on Fuzzy
Spatial Objects (FIFUS) for Spatial Decision Support Systems"
<doi:10.1109/FUZZ-IEEE.2017.8015707>.

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
