%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rsearch
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Processing and Analyzing Amplicon Sequence Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.8.1
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-microseq >= 2.1.6
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-cowplot >= 1.1.3
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-ggExtra >= 0.10.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape >= 5.8.1
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-microseq >= 2.1.6
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-cowplot >= 1.1.3
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-ggExtra >= 0.10.1
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
Processing and analysis of amplicon sequencing data, with a primary focus
on eDNA metabarcoding while remaining applicable to general targeted
sequencing workflows. The package provides a user-friendly interface for
core 'VSEARCH' (Rognes et al. (2016), <doi:10.7717/peerj.2584>) functions,
extended with dedicated tools for visualization and parameter tuning.

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
