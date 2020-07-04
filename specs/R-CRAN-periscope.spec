%global packname  periscope
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Enterprise Streamlined 'Shiny' Application Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 3.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-lubridate >= 1.6
BuildRequires:    R-CRAN-shiny >= 1.1
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-shinydashboard >= 0.5
BuildRequires:    R-CRAN-shinydashboardPlus >= 0.5
BuildRequires:    R-CRAN-DT >= 0.2
BuildRequires:    R-methods 
Requires:         R-CRAN-openxlsx >= 3.0
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-lubridate >= 1.6
Requires:         R-CRAN-shiny >= 1.1
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-shinydashboard >= 0.5
Requires:         R-CRAN-shinydashboardPlus >= 0.5
Requires:         R-CRAN-DT >= 0.2
Requires:         R-methods 

%description
An enterprise-targeted scalable and UI-standardized 'shiny' framework
including a variety of developer convenience functions with the goal of
both streamlining robust application development while assisting with
creating a consistent user experience regardless of application or
developer.

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
