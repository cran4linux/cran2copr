%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eclipseplot
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Visualizations for ROBUST-RCT Risk of Bias Assessments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readxl 

%description
Provides visual representations of risk-of-bias assessments using the
ROBUST-RCT framework, as described in Wang et al. (2025)
<doi:10.1136/bmj-2024-081199>. The graphical visualization displays both
factual evaluation (Step 1) and judgment (Step 2).

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
