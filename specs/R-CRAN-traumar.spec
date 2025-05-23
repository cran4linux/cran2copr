%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  traumar
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Metrics for Trauma System Performance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-lubridate >= 1.9.4
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-patchwork >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-hms >= 1.1.3
BuildRequires:    R-CRAN-nemsqar >= 1.1.0
BuildRequires:    R-CRAN-infer >= 1.0.8
BuildRequires:    R-CRAN-nortest >= 1.0.4
BuildRequires:    R-CRAN-purrr >= 1.0.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-lubridate >= 1.9.4
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-patchwork >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-hms >= 1.1.3
Requires:         R-CRAN-nemsqar >= 1.1.0
Requires:         R-CRAN-infer >= 1.0.8
Requires:         R-CRAN-nortest >= 1.0.4
Requires:         R-CRAN-purrr >= 1.0.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
Hospitals, hospital systems, and even trauma systems that provide care to
injured patients may not be aware of robust metrics that can help gauge
the efficacy of their programs in saving the lives of injured patients.
'traumar' provides robust functions driven by the academic literature to
automate the calculation of relevant metrics to individuals desiring to
measure the performance of their trauma center or even a trauma system.
'traumar' also provides some helper functions for the data analysis
journey. Users can refer to the following publications for descriptions of
the methods used in 'traumar'.  TRISS methodology, including probability
of survival, and the W, M, and Z Scores - Flora (1978)
<doi:10.1097/00005373-197810000-00003>, Boyd et al. (1987, PMID:3106646),
Llullaku et al. (2009) <doi:10.1186/1749-7922-4-2>, Singh et al. (2011)
<doi:10.4103/0974-2700.86626>, Baker et al. (1974, PMID:4814394), and
Champion et al. (1989) <doi:10.1097/00005373-198905000-00017>. For the
Relative Mortality Metric, see Napoli et al. (2017)
<doi:10.1080/24725579.2017.1325948>, Schroeder et al. (2019)
<doi:10.1080/10903127.2018.1489021>, and Kassar et al. (2016)
<doi:10.1177/00031348221093563>. For more information about methods to
calculate over- and under-triage in trauma hospital populations and
samples, please see the following publications - Peng & Xiang (2016)
<doi:10.1016/j.ajem.2016.08.061>, Beam et al. (2022)
<doi:10.23937/2474-3674/1510136>, Roden-Foreman et al. (2017)
<doi:10.1097/JTN.0000000000000283>.

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
