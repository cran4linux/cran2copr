%global packname  heatwaveR
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Detect Heatwaves and Cold-Spells

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zoo 
Requires:         R-grid 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 

%description
The different methods of defining and detecting extreme events, known as
heatwaves or cold-spells in both air and water temperature data are
encompassed within this package. These detection algorithms may be used on
non-temperature data as well however, this is not catered for explicitly
here as no use of this technique in the literature currently exists.

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
