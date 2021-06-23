%global __brp_check_rpaths %{nil}
%global packname  ezEDA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Task Oriented Interface for Exploratory Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-GGally >= 1.4.0
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-rlang >= 0.2.1
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-GGally >= 1.4.0
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-rlang >= 0.2.1

%description
Enables users to create visualizations using functions based on the data
analysis task rather than on plotting mechanics. It hides the details of
the individual 'ggplot2' function calls and allows the user to focus on
the end goal. Useful for quick preliminary explorations. Provides
functions for common exploration patterns. Some of the ideas in this
package are motivated by Fox (2015, ISBN:1938377052).

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
