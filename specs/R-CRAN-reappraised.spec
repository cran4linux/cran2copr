%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reappraised
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Assessing Publication Integrity of Groups of Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-vcdExtra 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-vcdExtra 

%description
Takes user-provided baseline data from groups of randomised controlled
data and assesses whether the observed distribution of baseline p-values,
numbers of participants in each group, or categorical variables are
consistent with the expected distribution, as an aid to the assessment of
integrity concerns in published randomised controlled trials. References
(citations in PubMed format in details of each function): Bolland MJ,
Avenell A, Gamble GD, Grey A. (2016) <doi:10.1212/WNL.0000000000003387>.
Bolland MJ, Gamble GD, Avenell A, Grey A, Lumley T. (2019)
<doi:10.1016/j.jclinepi.2019.05.006>. Bolland MJ, Gamble GD, Avenell A,
Grey A. (2019) <doi:10.1016/j.jclinepi.2019.03.001>. Bolland MJ, Gamble
GD, Grey A, Avenell A. (2020) <doi:10.1111/anae.15165>. Bolland MJ, Gamble
GD, Avenell A, Cooper DJ, Grey A. (2021)
<doi:10.1016/j.jclinepi.2020.11.012>. Bolland MJ, Gamble GD, Avenell A,
Grey A. (2021) <doi:10.1016/j.jclinepi.2021.05.002>. Bolland MJ, Gamble
GD, Avenell A, Cooper DJ, Grey A. (2023)
<doi:10.1016/j.jclinepi.2022.12.018>. Carlisle JB, Loadsman JA. (2017)
<doi:10.1111/anae.13650>. Carlisle JB. (2017) <doi:10.1111/anae.13938>.

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
