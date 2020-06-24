%global packname  ggforce
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Accelerating 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-tweenr >= 0.1.5
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-polyclip 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-tweenr >= 0.1.5
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-MASS 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-polyclip 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-withr 
Requires:         R-utils 

%description
The aim of 'ggplot2' is to aid in visual data investigations. This focus
has led to a lack of facilities for composing specialised plots. 'ggforce'
aims to be a collection of mainly new stats and geoms that fills this gap.
All additional functionality is aimed to come through the official
extension system so using 'ggforce' should be a stable experience.

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
