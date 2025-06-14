%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rock
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Open Coding Kit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-squids >= 25.5.3
BuildRequires:    R-CRAN-yaml >= 2.2.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-data.tree >= 1.1.0
BuildRequires:    R-CRAN-markdown >= 1.1
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-yum >= 0.1.0
BuildRequires:    R-CRAN-DiagrammeRsvg >= 0.1
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-squids >= 25.5.3
Requires:         R-CRAN-yaml >= 2.2.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-data.tree >= 1.1.0
Requires:         R-CRAN-markdown >= 1.1
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-yum >= 0.1.0
Requires:         R-CRAN-DiagrammeRsvg >= 0.1

%description
The Reproducible Open Coding Kit ('ROCK', and this package, 'rock') was
developed to facilitate reproducible and open coding, specifically geared
towards qualitative research methods. It was developed to be both human-
and machine-readable, in the spirit of MarkDown and 'YAML'. The idea is
that this makes it relatively easy to write other functions and packages
to process 'ROCK' files. The 'rock' package contains functions for basic
coding and analysis, such as collecting and showing coded fragments and
prettifying sources, as well as a number of advanced analyses such as the
Qualitative Network Approach and Qualitative/Unified Exploration of State
Transitions. The 'ROCK' and this 'rock' package are described in the ROCK
book (Zörgő & Peters, 2022; <https://rockbook.org>), in Zörgő & Peters
(2024) <doi:10.1080/21642850.2022.2119144> and Peters, Zörgő and van der
Maas (2022) <doi:10.31234/osf.io/cvf52>, and more information and
tutorials are available at <https://rock.science>.

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
