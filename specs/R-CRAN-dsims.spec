%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsims
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distance Sampling Simulations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dssd >= 0.2.2
BuildRequires:    R-CRAN-mrds 
BuildRequires:    R-CRAN-Distance 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dssd >= 0.2.2
Requires:         R-CRAN-mrds 
Requires:         R-CRAN-Distance 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-rgeos 
Requires:         R-methods 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rlang 

%description
Performs distance sampling simulations. 'dsims' repeatedly generates
instances of a user defined population within a given survey region. It
then generates realisations of a survey design and simulates the detection
process. The data are then analysed so that the results can be compared
for accuracy and precision across all replications. This process allows
users to optimise survey designs for their specific set of survey
conditions. The effects of uncertainty in population distribution or
parameters can be investigated under a number of simulations so that users
can be confident that they have achieved a robust survey design before
deploying vessels into the field. The distance sampling designs used in
this package from 'dssd' are detailed in Chapter 7 of Advanced Distance
Sampling, Buckland et. al. (2008, ISBN-13: 978-0199225873). General
distance sampling methods are detailed in Introduction to Distance
Sampling: Estimating Abundance of Biological Populations, Buckland et. al.
(2004, ISBN-13: 978-0198509271). Find out more about estimating
animal/plant abundance with distance sampling at
<http://distancesampling.org/>.

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
