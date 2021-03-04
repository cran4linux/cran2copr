%global packname  popPCR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classify Digital PCR Droplets by Fitting Fluorescence Populations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-KernSmooth 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-KernSmooth 

%description
Estimates DNA target concentration by classifying digital PCR (polymerase
chain reaction) droplets as positive, negative, or rain, using
Expectation-Maximization Clustering. The fitting is accomplished using the
'EMMIXskew' R package (v. 1.0.3) by Kui Wang, Angus Ng, and Geoff
McLachlan (2018) as based on their paper "Multivariate Skew t Mixture
Models: Applications to Fluorescence-Activated Cell Sorting Data"
<doi:10.1109/DICTA.2009.88>.

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
