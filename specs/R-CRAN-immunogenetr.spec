%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  immunogenetr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Toolkit for Clinical HLA Informatics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.3
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-xml2 >= 1.3.6
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.1
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-tibble >= 3.1.3
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-xml2 >= 1.3.6
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.1.1
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-cli >= 1.0.0

%description
A comprehensive toolkit for clinical Human Leukocyte Antigen (HLA)
informatics, built on 'tidyverse' <https://tidyverse.tidyverse.org/>
principles and making use of genotype list string (GL string, Mack et al.
(2023) <doi:10.1111/tan.15126>) for storing and computing HLA genotype
data.  Specific functionalities include: coercion of HLA data in tabular
format to and from GL string; calculation of matching and mismatching in
all directions, with multiple output formats; automatic formatting of HLA
data for searching within a GL string; truncation of molecular HLA data to
a specific number of fields; and reading HLA genotypes in HML files and
extracting the GL string.

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
