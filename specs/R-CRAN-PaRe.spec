%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PaRe
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          A Way to Perform Code Review or QA on Other Packages

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-lintr >= 3.0.2
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-rsvg >= 2.4.0
BuildRequires:    R-CRAN-rmarkdown >= 2.20
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-desc >= 1.4.2
BuildRequires:    R-CRAN-igraph >= 1.3.5
BuildRequires:    R-CRAN-cyclocomp >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.9
BuildRequires:    R-CRAN-git2r >= 0.31.0
BuildRequires:    R-CRAN-pak >= 0.2.0
BuildRequires:    R-CRAN-DiagrammeRsvg >= 0.1
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-lintr >= 3.0.2
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-rsvg >= 2.4.0
Requires:         R-CRAN-rmarkdown >= 2.20
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-desc >= 1.4.2
Requires:         R-CRAN-igraph >= 1.3.5
Requires:         R-CRAN-cyclocomp >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-DiagrammeR >= 1.0.9
Requires:         R-CRAN-git2r >= 0.31.0
Requires:         R-CRAN-pak >= 0.2.0
Requires:         R-CRAN-DiagrammeRsvg >= 0.1
Requires:         R-utils 

%description
Reviews other packages during code review by looking at their
dependencies, code style, code complexity, and how internally defined
functions interact with one another.

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
