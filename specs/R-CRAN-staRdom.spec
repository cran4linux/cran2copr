%global packname  staRdom
%global packver   1.1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.14
Release:          1%{?dist}%{?buildtag}
Summary:          PARAFAC Analysis of EEMs from DOM

License:          AGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.8.2
BuildRequires:    R-CRAN-R.matlab >= 3.6.2
BuildRequires:    R-parallel >= 3.6
BuildRequires:    R-graphics >= 3.6
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.0.3
BuildRequires:    R-CRAN-drc >= 3.0.1
BuildRequires:    R-CRAN-pracma >= 2.2.9
BuildRequires:    R-CRAN-GGally >= 2.0.0
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-multiway >= 1.0.6
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-eemR >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-matrixStats >= 0.56.0
BuildRequires:    R-CRAN-cdom >= 0.1.0
BuildRequires:    R-CRAN-MBA >= 0.0.9
Requires:         R-CRAN-gtools >= 3.8.2
Requires:         R-CRAN-R.matlab >= 3.6.2
Requires:         R-parallel >= 3.6
Requires:         R-graphics >= 3.6
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-tibble >= 3.0.3
Requires:         R-CRAN-drc >= 3.0.1
Requires:         R-CRAN-pracma >= 2.2.9
Requires:         R-CRAN-GGally >= 2.0.0
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-multiway >= 1.0.6
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-eemR >= 1.0.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-matrixStats >= 0.56.0
Requires:         R-CRAN-cdom >= 0.1.0
Requires:         R-CRAN-MBA >= 0.0.9

%description
This is a user-friendly way to run a parallel factor (PARAFAC) analysis
(Harshman, 1971) <doi:10.1121/1.1977523> on excitation emission matrix
(EEM) data from dissolved organic matter (DOM) samples (Murphy et al.,
2013) <doi:10.1039/c3ay41160e>. The analysis includes profound methods for
model validation. Some additional functions allow the calculation of
absorbance slope parameters and create beautiful plots.

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
