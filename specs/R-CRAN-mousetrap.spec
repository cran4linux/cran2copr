%global packname  mousetrap
%global packver   3.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.4
Release:          1%{?dist}
Summary:          Process and Analyze Mouse-Tracking Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-psych >= 1.2.4
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-cstab 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-psych >= 1.2.4
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-cstab 
Requires:         R-CRAN-fastcluster 
Requires:         R-parallel 
Requires:         R-CRAN-fields 

%description
Mouse-tracking, the analysis of mouse movements in computerized
experiments, is a method that is becoming increasingly popular in the
cognitive sciences. The mousetrap package offers functions for importing,
preprocessing, analyzing, aggregating, and visualizing mouse-tracking
data.

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
