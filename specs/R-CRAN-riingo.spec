%global __brp_check_rpaths %{nil}
%global packname  riingo
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          An R Interface to the 'Tiingo' Stock Price API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rlang >= 0.2.0

%description
Functionality to download stock prices, cryptocurrency data, and more from
the 'Tiingo' API <https://api.tiingo.com/>.

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
