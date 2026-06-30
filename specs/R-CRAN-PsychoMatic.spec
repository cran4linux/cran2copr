%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PsychoMatic
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Psychometric Workflows and Reporting Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-utils 

%description
Automates common psychometric workflows for applied researchers, including
item descriptives, inter-item correlations, exploratory and confirmatory
factor analysis, reliability, multi-group measurement invariance, and
alignment optimization. Decision heuristics are informed by procedures
such as parallel analysis (Horn, 1965, <doi:10.1007/BF02289447>),
multivariate normality diagnostics (Mardia, 1970,
<doi:10.1093/biomet/57.3.519>), measurement-invariance fit-change rules
(Chen, 2007, <doi:10.1080/10705510701301834>), and alignment optimization
(Asparouhov and Muthen, 2014, <doi:10.1080/10705511.2014.919210>), among
others. Results can be returned as structured R objects and exported as
bilingual reports for transparent analytical documentation.

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
