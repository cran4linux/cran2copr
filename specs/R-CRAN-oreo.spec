%global __brp_check_rpaths %{nil}
%global packname  oreo
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Large Amplitude Oscillatory Shear (LAOS)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-spectral 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-fftwtools 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-openxlsx 
Requires:         R-tools 
Requires:         R-CRAN-spectral 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-fftwtools 
Requires:         R-CRAN-scales 

%description
The Sequence of Physical Processes (SPP) framework is a way of
interpreting the transient data derived from oscillatory rheological
tests. It is designed to allow both the linear and non-linear deformation
regimes to be understood within a single unified framework. This code
provides a convenient way to determine the SPP framework metrics for a
given sample of oscillatory data. It will produce a text file containing
the SPP metrics, which the user can then plot using their software of
choice. It can also produce a second text file with additional derived
data (components of tangent, normal, and binormal vectors), as well as
pre-plotted figures if so desired. It is the R version of the Package SPP
by Simon Rogers Group for Soft Matter (Simon A. Rogers, Brian M. Erwin,
Dimitris Vlassopoulos, Michel Cloitre (2011) <doi:10.1122/1.3544591>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
