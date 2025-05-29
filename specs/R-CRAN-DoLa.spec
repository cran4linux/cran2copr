%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DoLa
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Do Currículo Lattes Para o Programa de Pós-Graduação

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 

%description
Managing postgraduate programmes involves extracting information from
Lattes CVs. This information can be used for strategic planning and
self-evaluation, as well as for producing reports on the Sucupira
Platform. Summary reports are produced for each period and course
(specialisation, master's and doctorate), showing bibliographic production
with and without student participation, as well as papers at events,
technical or technological production, ongoing and completed supervision,
research projects, exchanges (visiting professor, postdoctoral or
short-term leave), awards and general activity indicators. Based on this
information, a detailed report is then drawn up for each lecturer, taking
into account their participation in exam boards, their research project
contributions, their technical collaborations (e.g. advisory committee,
editorial board) and the subjects they teach. For more details see
Pagliosa and Nascimento (2021)
<https://repositorio.ufsc.br/bitstream/handle/123456789/231602/ManualLattesGeociencias11_2021_versaobeta%%20%%281%%29.pdf?sequence=1&isAllowed=y>.

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
