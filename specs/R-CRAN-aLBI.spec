%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aLBI
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Length-Based Indicators for Fish Stock

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-openxlsx 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 

%description
Provides tools for estimating length-based indicators from length
frequency data to assess fish stock status and manage fisheries
sustainably. Implements methods from Cope and Punt (2009)
<doi:10.1577/C08-025.1> for data-limited stock assessment and Froese
(2004) <doi:10.1111/j.1467-2979.2004.00144.x> for detecting overfishing
using simple indicators. Key functions include: FrequencyTable():
Calculate the frequency table from the collected and also the extract the
length frequency data from the frequency table with the upper
length_range. A numeric value specifying the bin width for class
intervals. If not provided, the bin width is automatically calculated
using Sturges (1926) <doi:10.1080/01621459.1926.10502161> formula.
CalPar(): Calculates various lengths used in fish stock assessment as
biological length indicators such as asymptotic length (Linf), maximum
length (Lmax), length at sexual maturity (Lm), and optimal length (Lopt).
FishPar(): Calculates length-based indicators (LBIs) proposed by Froese
(2004) <doi:10.1111/j.1467-2979.2004.00144.x> such as the percentage of
mature fish (Pmat), percentage of optimal length fish (Popt), percentage
of mega spawners (Pmega), and the sum of these as Pobj. This function also
estimates confidence intervals for different lengths, visualizes length
frequency distributions, and provides data frames containing calculated
values. FishSS(): Makes decisions based on input from Cope and Punt (2009)
<doi:10.1577/C08-025.1> and parameters calculated by FishPar() (e.g.,
Pobj, Pmat, Popt, LM_ratio) to determine stock status as target spawning
biomass (TSB40) and limit spawning biomass (LSB25). LWR(): Fits and
visualizes length-weight relationships using linear regression, with
options for log-transformation and customizable plotting.

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
