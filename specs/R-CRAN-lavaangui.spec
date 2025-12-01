%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lavaangui
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical User Interface with Integrated 'Diagrammer' for 'Lavaan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods >= 4.3.3
BuildRequires:    R-tools >= 4.3.3
BuildRequires:    R-utils >= 4.3.3
BuildRequires:    R-CRAN-haven >= 2.5.3
BuildRequires:    R-CRAN-readr >= 2.1.4
BuildRequires:    R-CRAN-colorspace >= 2.1.0
BuildRequires:    R-CRAN-igraph >= 2.0.3
BuildRequires:    R-CRAN-plyr >= 1.8.9
BuildRequires:    R-CRAN-jsonlite >= 1.8.4
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-CRAN-future >= 1.33.0
BuildRequires:    R-CRAN-promises >= 1.2.0.1
BuildRequires:    R-CRAN-digest >= 0.6.35
BuildRequires:    R-CRAN-lavaan >= 0.6.20
BuildRequires:    R-CRAN-DT >= 0.33
BuildRequires:    R-CRAN-base64enc >= 0.1.3
Requires:         R-methods >= 4.3.3
Requires:         R-tools >= 4.3.3
Requires:         R-utils >= 4.3.3
Requires:         R-CRAN-haven >= 2.5.3
Requires:         R-CRAN-readr >= 2.1.4
Requires:         R-CRAN-colorspace >= 2.1.0
Requires:         R-CRAN-igraph >= 2.0.3
Requires:         R-CRAN-plyr >= 1.8.9
Requires:         R-CRAN-jsonlite >= 1.8.4
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-CRAN-future >= 1.33.0
Requires:         R-CRAN-promises >= 1.2.0.1
Requires:         R-CRAN-digest >= 0.6.35
Requires:         R-CRAN-lavaan >= 0.6.20
Requires:         R-CRAN-DT >= 0.33
Requires:         R-CRAN-base64enc >= 0.1.3

%description
Provides a graphical user interface with an integrated diagrammer for
latent variable models from the 'lavaan' package. It offers two core
functions: first, lavaangui() launches a web application that allows users
to specify models by drawing path diagrams, fitting them, assessing model
fit, and more; second, plot_lavaan() creates interactive path diagrams
from models specified in 'lavaan'. Karch (2024) <doi:
10.1080/10705511.2024.2420678> contains a tutorial.

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
