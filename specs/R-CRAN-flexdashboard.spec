%global __brp_check_rpaths %{nil}
%global packname  flexdashboard
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          2%{?dist}%{?buildtag}
Summary:          R Markdown Format for Flexible Dashboards

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.13
BuildRequires:    R-CRAN-rmarkdown >= 1.10
BuildRequires:    R-CRAN-htmlwidgets >= 0.6
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-knitr >= 1.13
Requires:         R-CRAN-rmarkdown >= 1.10
Requires:         R-CRAN-htmlwidgets >= 0.6
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-tools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-htmltools 

%description
Format for converting an R Markdown document to a grid oriented dashboard.
The dashboard flexibly adapts the size of it's components to the
containing web page.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
