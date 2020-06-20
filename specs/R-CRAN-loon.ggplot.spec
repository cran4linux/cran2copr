%global packname  loon.ggplot
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Making 'ggplot2' Plots Interactive with 'loon' and Vice Versa

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-loon > 1.2.3
BuildRequires:    R-tcltk 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-loon > 1.2.3
Requires:         R-tcltk 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-stringr 
Requires:         R-grid 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 

%description
It provides a bridge between the 'loon' and 'ggplot2' packages. Data
analysts who value the grammar pipeline provided by 'ggplot2' can turn
these static plots into interactive 'loon' plots. Conversely, data
analysts who explore data interactively with 'loon' can turn any 'loon'
plot into a 'ggplot2' plot structure. The function 'loon.ggplot()' is
applied to one plot structure will return the other.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
