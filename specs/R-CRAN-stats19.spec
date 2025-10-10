%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stats19
%global packver   3.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Work with Open Road Traffic Casualty Data from Great Britain

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-curl >= 3.2
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-jsonlite 

%description
Work with and download road traffic casualty data from Great Britain.
Enables access to the UK's official road safety statistics, 'STATS19'.
Enables users to specify a download directory for the data, which can be
set permanently by adding `STATS19_DOWNLOAD_DIRECTORY=/path/to/a/dir` to
your `.Renviron` file, which can be opened with
`usethis::edit_r_environ()`. The data is provided as a series of `.csv`
files. This package downloads, reads-in and formats the data, making it
suitable for analysis. See the stats19 vignette for details. Data
available from 1979 to 2024. See the official data series at
<https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-accidents-safety-data>.
The package is described in a paper in the Journal of Open Source Software
(Lovelace et al. 2019) <doi:10.21105/joss.01181>. See Gilardi et al.
(2022) <doi:10.1111/rssa.12823>, Vidal-Tortosa et al. (2021)
<doi:10.1016/j.jth.2021.101291>, Tait et al. (2023)
<doi:10.1016/j.aap.2022.106895>, and León et al. (2025)
<doi:10.18637/jss.v114.i09> for examples of how the data can be used for
methodological and empirical research.

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
