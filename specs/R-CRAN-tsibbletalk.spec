%global packname  tsibbletalk
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Graphics for Tsibble Objects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.2.1
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.4.1
BuildRequires:    R-CRAN-dendextend >= 1.13.4
BuildRequires:    R-CRAN-crosstalk >= 1.1.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tsibble >= 0.9.1
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-vctrs >= 0.3.1
Requires:         R-CRAN-plotly >= 4.9.2.1
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-glue >= 1.4.1
Requires:         R-CRAN-dendextend >= 1.13.4
Requires:         R-CRAN-crosstalk >= 1.1.0.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tsibble >= 0.9.1
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-vctrs >= 0.3.1

%description
A shared tsibble data easily communicates between htmlwidgets on both
client and server sides, powered by 'crosstalk'. A shiny module is
provided to visually explore periodic/aperiodic temporal patterns.

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
