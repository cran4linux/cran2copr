%global packname  augmentedRCBD
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Analysis of Augmented Randomised Complete Block Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-utils 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-reshape2 
Requires:         R-utils 

%description
Functions for analysis of data generated from experiments in augmented
randomised complete block design according to Federer, W.T. (1961)
<doi:10.2307/2527837>. Computes analysis of variance, adjusted means,
descriptive statistics, genetic variability statistics etc. Further
includes data visualization and report generation functions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
