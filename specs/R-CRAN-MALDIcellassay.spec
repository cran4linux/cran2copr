%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MALDIcellassay
%global packver   0.4.47
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.47
Release:          1%{?dist}%{?buildtag}
Summary:          Automated MALDI Cell Assays Using Dose-Response Curve Fitting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nplr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-MALDIquant 
BuildRequires:    R-CRAN-MALDIquantForeign 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-svMisc 
BuildRequires:    R-CRAN-purrr 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nplr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-MALDIquant 
Requires:         R-CRAN-MALDIquantForeign 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-svMisc 
Requires:         R-CRAN-purrr 

%description
Conduct automated cell-based assays using Matrix-Assisted Laser
Desorption/Ionization (MALDI) methods for high-throughput screening of
signals responsive to treatments. The package efficiently identifies high
variance signals and fits dose-response curves to them. Quality metrics
such as Z', V', log2FC, and CRS are provided for evaluating the potential
of signals as biomarkers. The methodologies were introduced by Weigt et
al. (2018) <doi:10.1038/s41598-018-29677-z> and refined by Unger et al.
(2021) <doi:10.1038/s41596-021-00624-z>.

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
