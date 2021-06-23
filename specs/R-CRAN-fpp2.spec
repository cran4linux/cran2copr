%global __brp_check_rpaths %{nil}
%global packname  fpp2
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Data for "Forecasting: Principles and Practice" (2nd Edition)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-expsmooth 
BuildRequires:    R-CRAN-fma 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-forecast >= 8.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-expsmooth 
Requires:         R-CRAN-fma 
Requires:         R-CRAN-ggplot2 

%description
All data sets required for the examples and exercises in the book
"Forecasting: principles and practice" (2nd ed, 2018) by Rob J Hyndman and
George Athanasopoulos <https://otexts.com/fpp2/>. All packages required to
run the examples are also loaded.

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
