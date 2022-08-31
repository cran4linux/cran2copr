%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TestDimorph
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of the Interpopulation Difference in Degree of Sexual Dimorphism Using Summary Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Morpho 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Morpho 
Requires:         R-CRAN-multcompView 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
Offers a solution for the unavailability of raw data in most
anthropological studies by facilitating the calculations of several sexual
dimorphism related analyses using the published summary statistics of
metric data (mean, standard deviation and sex specific sample size) as
illustrated by the works of Relethford, J. H., & Hodges, D. C. (1985)
<doi:10.1002/ajpa.1330660105>, Greene, D. L. (1989)
<doi:10.1002/ajpa.1330790113> and Konigsberg, L. W. (1991)
<doi:10.1002/ajpa.1330840110>.

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
