%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BinMat
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Processes Binary Data Obtained from Fragment Analysis (Such as AFLPs, ISSRs, and RFLPs)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-base >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.1.4
BuildRequires:    R-CRAN-pvclust >= 2.0
BuildRequires:    R-CRAN-ggpubr >= 0.4.0
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-stats >= 3.4.0
Requires:         R-graphics >= 3.4.0
Requires:         R-base >= 3.4.0
Requires:         R-CRAN-tibble >= 3.1.4
Requires:         R-CRAN-pvclust >= 2.0
Requires:         R-CRAN-ggpubr >= 0.4.0

%description
A molecular genetics tool that processes binary data from fragment
analysis. It consolidates replicate sample pairs, outputs summary
statistics, and produces hierarchical clustering trees and nMDS plots.
This package was developed from the publication available here:
<doi:10.1016/j.biocontrol.2020.104426>. The GUI version of this package is
available on the R Shiny online server at:
<https://clarkevansteenderen.shinyapps.io/BINMAT/> or it is accessible via
GitHub by typing: shiny::runGitHub("BinMat", "clarkevansteenderen") into
the console in R. Two real-world datasets accompany the package: an AFLP
dataset of Bunias orientalis samples from Tewes et. al. (2017)
<doi:10.1111/1365-2745.12869>, and an ISSR dataset of Nymphaea specimens
from Reid et. al. (2021) <doi:10.1016/j.aquabot.2021.103372>. The authors
of these publications are thanked for allowing the use of their data.

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
