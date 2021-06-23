%global __brp_check_rpaths %{nil}
%global packname  shiny.i18n
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shiny Applications Internationalization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rstudioapi 
Requires:         R-utils 

%description
It provides easy internationalization of Shiny applications. It can be
used as standalone translation package to translate reports, interactive
visualizations or graphical elements as well.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
