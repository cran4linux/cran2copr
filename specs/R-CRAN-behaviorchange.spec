%global __brp_check_rpaths %{nil}
%global packname  behaviorchange
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Behavior Change Researchers and Professionals

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-BiasedUrn >= 1.07
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-knitr >= 1.0
BuildRequires:    R-CRAN-data.tree >= 0.7.5
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-rmdpartials >= 0.5.0
BuildRequires:    R-CRAN-ufs >= 0.3.2
BuildRequires:    R-CRAN-googlesheets4 >= 0.2.0
BuildRequires:    R-CRAN-gtable >= 0.2.0
BuildRequires:    R-CRAN-DiagrammeRsvg >= 0.1
BuildRequires:    R-CRAN-yum >= 0.0.1
Requires:         R-methods >= 3.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-BiasedUrn >= 1.07
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-knitr >= 1.0
Requires:         R-CRAN-data.tree >= 0.7.5
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-rmdpartials >= 0.5.0
Requires:         R-CRAN-ufs >= 0.3.2
Requires:         R-CRAN-googlesheets4 >= 0.2.0
Requires:         R-CRAN-gtable >= 0.2.0
Requires:         R-CRAN-DiagrammeRsvg >= 0.1
Requires:         R-CRAN-yum >= 0.0.1

%description
Contains specialised analyses and visualisation tools for behavior change
science. These facilitate conducting determinant studies (for example,
using confidence interval-based estimation of relevance, CIBER, or
CIBERlite plots, see Crutzen, Noijen & Peters (2017)
<doi:10.3389/fpubh.2017.00165>), systematically developing, reporting, and
analysing interventions (for example, using Acyclic Behavior Change
Diagrams), and reporting about intervention effectiveness (for example,
using the Numbers Needed for Change, see Gruijters & Peters (2017)
<doi:10.31234/osf.io/2bau7>), and computing the required sample size
(using the Meaningful Change Definition, see Gruijters & Peters (2019)
<doi:10.31234/osf.io/jc295>). This package is especially useful for
researchers in the field of behavior change or health psychology and to
behavior change professionals such as intervention developers and
prevention workers.

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
