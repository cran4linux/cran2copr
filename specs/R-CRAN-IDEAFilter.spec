%global __brp_check_rpaths %{nil}
%global packname  IDEAFilter
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Agnostic, Idiomatic Data Filter Module for Shiny

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pillar >= 1.5.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-shinyTime 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-pillar >= 1.5.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-shinyTime 
Requires:         R-CRAN-purrr 

%description
When added to an existing shiny app, users may subset any developer-chosen
R data.frame on the fly. That is, users are empowered to slice & dice data
by applying multiple (order specific) filters using the AND (&) operator
between each, and getting real-time updates on the number of rows
effected/available along the way. Thus, any downstream processes that
leverage this data source (like tables, plots, or statistical procedures)
will re-render after new filters are applied. The shiny module’s user
interface has a 'minimalist' aesthetic so that the focus can be on the
data & other visuals. In addition to returning a reactive (filtered)
data.frame, 'IDEAFilter' as also returns 'dplyr' filter statements used to
actually slice the data.

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
