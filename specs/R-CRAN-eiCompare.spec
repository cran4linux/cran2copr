%global __brp_check_rpaths %{nil}
%global packname  eiCompare
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compares Ecological Inference, Goodman, Rows by Columns Estimates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-eiPack 
BuildRequires:    R-CRAN-ei 
BuildRequires:    R-CRAN-wru 
BuildRequires:    R-CRAN-censusxy 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-overlapping 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-eiPack 
Requires:         R-CRAN-ei 
Requires:         R-CRAN-wru 
Requires:         R-CRAN-censusxy 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mcmcse 
Requires:         R-methods 
Requires:         R-CRAN-overlapping 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-tidyselect 

%description
Compares estimates from three ecological inference routines, based on King
(1997) <ISBN: 0691012407>,
<https://gking.harvard.edu/eicamera/kinroot.html>; King (2004) <ISBN:
0521542804>, <https://gking.harvard.edu/files/abs/ecinf04-abs.shtml>.

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
