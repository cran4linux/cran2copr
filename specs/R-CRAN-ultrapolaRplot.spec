%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ultrapolaRplot
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Plotting Ultrasound Tongue Traces

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 

%description
Plots traced ultrasound tongue imaging data according to a polar
coordinate system. There is currently support for plotting means and
standard deviations of each category's trace; Smoothing Splines Analysis
of Variance (SSANOVA) could be implemented as well.  The origin of the
polar coordinates may be defined manually or automatically determined
based on different algorithms. Currently 'ultrapolaRplot' supports
ultrasound tongue imaging trace data from 'UltraTrace'
(<https://github.com/SwatPhonLab/UltraTrace>). 'UltraTrace' is capable of
importing data from Articulate Instruments AAA. 'read_textgrid.R' is
required for opening TextGrids to determine category and alignment
information of ultrasound traces.

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
