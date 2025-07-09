%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  door
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Clinical Trials with the Desirability of Outcome Ranking Methodology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-labeling 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-scales 
Requires:         R-methods 
Requires:         R-CRAN-labeling 

%description
Statistical methods and related graphical representations for the
Desirability of Outcome Ranking (DOOR) methodology. The DOOR is a paradigm
for the design, analysis, interpretation of clinical trials and other
research studies based on the patient centric benefit risk evaluation. The
package provides functions for generating summary statistics from
individual level/summary level datasets, conduct DOOR probability-based
inference, and visualization of the results. For more details of DOOR
methodology, see Hamasaki and Evans (2025) <doi:10.1201/9781003390855>.
For more explanation of the statistical methods and the graphics, see the
technical document and user manual of the DOOR 'Shiny' apps at
<https://methods.bsc.gwu.edu>.

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
