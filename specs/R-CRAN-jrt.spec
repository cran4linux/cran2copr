%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jrt
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Item Response Theory Modeling and Scoring for Judgment Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-directlabels >= 2021.1.13
BuildRequires:    R-CRAN-ggsci >= 2.9
BuildRequires:    R-CRAN-psych >= 2.1.9
BuildRequires:    R-CRAN-mirt >= 1.34
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-irr >= 0.84.1
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-directlabels >= 2021.1.13
Requires:         R-CRAN-ggsci >= 2.9
Requires:         R-CRAN-psych >= 2.1.9
Requires:         R-CRAN-mirt >= 1.34
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-irr >= 0.84.1
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Psychometric analysis and scoring of judgment data using polytomous
Item-Response Theory (IRT) models, as described in Myszkowski and Storme
(2019) <doi:10.1037/aca0000225> and Myszkowski (2021)
<doi:10.1037/aca0000287>. A function is used to automatically compare and
select models, as well as to present a variety of model-based statistics.
Plotting functions are used to present category curves, as well as
information, reliability and standard error functions.

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
