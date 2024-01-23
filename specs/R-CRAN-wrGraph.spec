%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wrGraph
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Graphics in the Context of Analyzing High-Throughput Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wrMisc 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-CRAN-wrMisc 

%description
Additional options for making graphics in the context of analyzing
high-throughput data are available here. This includes automatic
segmenting of the current device (eg window) to accommodate multiple new
plots, automatic checking for optimal location of legends in plots, small
histograms to insert as legends, histograms re-transforming axis labels to
linear when plotting log2-transformed data, a violin-plot
<doi:10.1080/00031305.1998.10480559> function for a wide variety of
input-formats, principal components analysis (PCA)
<doi:10.1080/14786440109462720> with bag-plots
<doi:10.1080/00031305.1999.10474494> to highlight and compare the center
areas for groups of samples, generic MA-plots (differential- versus
average-value plots) <doi:10.1093/nar/30.4.e15>, staggered count plots and
generation of mouse-over interactive html pages.

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
