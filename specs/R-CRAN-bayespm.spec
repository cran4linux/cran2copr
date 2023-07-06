%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayespm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Statistical Process Monitoring

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-invgamma 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-invgamma 

%description
The methods utilize available prior information and/or historical data,
providing efficient online quality monitoring of a process, in terms of
identifying moderate/large transient shifts (i.e., outliers) in the
process. These self-starting, sequentially updated tools can also run
under complete absence of any prior information. The Predictive Control
Chart (PCC) mechanism is introduced for the quality monitoring of data
from any discrete or continuous distribution that is a member of the
regular exponential family. Apart from monitoring, PCC allows also to
derive sequentially updated posterior inference for the monitored
parameter. Bourazas K., Kiagias D. and Tsiamyrtzis P. (2022) "Predictive
Control Charts (PCC): A Bayesian approach in online monitoring of short
runs" <doi:10.1080/00224065.2021.1916413>.

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
