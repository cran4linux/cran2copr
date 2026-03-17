%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MSMGOptimizer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mine Sustainability Modeling Group (MSMG) 'SimaPro' CSV Optimizer

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zip >= 2.3.0
BuildRequires:    R-CRAN-readxl >= 1.4.5
BuildRequires:    R-CRAN-shiny >= 1.10.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-shinydashboard >= 0.7.3
BuildRequires:    R-CRAN-htmltools >= 0.5.8.1
BuildRequires:    R-CRAN-DT >= 0.33
BuildRequires:    R-CRAN-waiter >= 0.2.5
Requires:         R-CRAN-zip >= 2.3.0
Requires:         R-CRAN-readxl >= 1.4.5
Requires:         R-CRAN-shiny >= 1.10.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-shinydashboard >= 0.7.3
Requires:         R-CRAN-htmltools >= 0.5.8.1
Requires:         R-CRAN-DT >= 0.33
Requires:         R-CRAN-waiter >= 0.2.5

%description
A 'Shiny' application for converting 'Excel'-based Life Cycle Inventory
(LCI) data into 'SimaPro' CSV (Comma-Separated Values) format for use in
Life Cycle Assessment (LCA) modeling. Developed by the Mine Sustainability
Modeling Group (MSMG) at Missouri University of Science and Technology
under NSF (National Science Foundation) funding (Award No. 2219086). See
Pizzol (2022) <https://github.com/massimopizzol/Simapro-CSV-converter> for
the original 'Python' implementation that inspired this tool.

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
