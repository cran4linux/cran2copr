%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggspec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extract and Compare 'ggplot2' Plot Specifications as Tidy Data Frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.1.0

%description
Inspects 'ggplot' objects by extracting their full declarative
specification - layers, aesthetic mappings, scales, facets, coordinate
systems, and labels - as tidy data frames. A second tier of functions
enables structural comparison of two 'ggplot' objects, supporting
automated plot testing, auditing, and framework-agnostic grading
workflows. Unlike 'ggcheck', which is designed exclusively for
'learnr'/'gradethis' pipelines and returns ad-hoc objects, 'ggspec'
returns rectangular, pipeable output and does not require any grading
framework as a dependency.

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
