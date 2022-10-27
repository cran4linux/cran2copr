%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyHugePlot
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Plotting of Large-Sized Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.0
BuildRequires:    R-CRAN-bit64 >= 4.0.5
BuildRequires:    R-CRAN-tibble >= 3.1.7
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-tidyselect >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.5
BuildRequires:    R-CRAN-htmltools >= 0.5.2
BuildRequires:    R-CRAN-nanotime >= 0.3.6
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-lazyeval >= 0.2.2
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-plotly >= 4.10.0
Requires:         R-CRAN-bit64 >= 4.0.5
Requires:         R-CRAN-tibble >= 3.1.7
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-tidyselect >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.5
Requires:         R-CRAN-htmltools >= 0.5.2
Requires:         R-CRAN-nanotime >= 0.3.6
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-lazyeval >= 0.2.2
Requires:         R-CRAN-assertthat >= 0.2.1

%description
A tool to plot data with large sample size using 'shiny' and 'plotly'.
Relatively small samples are chosen from the data using an appropriate
algorithm according to a user-defined x range. Jonas Van Der Donckt,
Jeroen Van Der Donckt, Emiel Deprost (2022)
<https://github.com/predict-idlab/plotly-resampler>.

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
