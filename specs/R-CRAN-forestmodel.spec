%global packname  forestmodel
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Forest Plots from Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-broom >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-broom >= 0.5.0
Requires:         R-CRAN-rlang >= 0.3.0

%description
Produces forest plots using 'ggplot2' from models produced by functions
such as stats::lm(), stats::glm() and survival::coxph().

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
