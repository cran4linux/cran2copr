%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCFMonitor
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Clear Monitor and Graphing Software Processing Gaussian .log File

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 

%description
Self-Consistent Field(SCF) calculation method is one of the most important
steps in the calculation methods of quantum chemistry. Ehrenreich, H., &
Cohen, M. H. (1959). <doi:10.1103/PhysRev.115.786> However, the most
prevailing software in this area, 'Gaussian''s SCF convergence process is
hard to monitor, especially while the job is still running, causing
researchers difficulty in knowing whether the oscillation has started or
not, wasting time and energy on useless configurations or abandoning the
jobs that can actually work. M.J. Frisch, G.W. Trucks, H.B. Schlegel et
al. (2016). <https://gaussian.com> 'SCFMonitor' enables 'Gaussian' quantum
chemistry calculation software users to easily read the 'Gaussian' .log
files and monitor the SCF convergence and geometry optimization process
with little effort and clear, beautiful, and clean outputs. It can
generate graphs using 'tidyverse' to let users check SCF convergence and
geometry optimization processes in real-time. The software supports
processing .log files remotely using with rbase::url(). This software is a
suitcase for saving time and energy for the researchers, supporting
multiple versions of 'Gaussian'.

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
