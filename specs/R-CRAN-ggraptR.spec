%global packname  ggraptR
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Allows Interactive Visualization of Data Through a Web BrowserGUI

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-pacman >= 0.4.6
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-shiny >= 0.12.2
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-pacman >= 0.4.6
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-shiny >= 0.12.2

%description
Intended for both technical and non-technical users to create interactive
data visualizations through a web browser GUI without writing any code.

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
