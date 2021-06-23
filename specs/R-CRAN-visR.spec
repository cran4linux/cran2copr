%global __brp_check_rpaths %{nil}
%global packname  visR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clinical Graphs and Tables Adhering to Graphical Principles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gt >= 0.1.0
BuildRequires:    R-CRAN-parcats >= 0.0.1
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-gt >= 0.1.0
Requires:         R-CRAN-parcats >= 0.0.1
Requires:         R-CRAN-broom 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rlang 

%description
To enable fit-for-purpose, reusable clinical and medical research focused
visualizations and tables with sensible defaults and based on graphical
principles as described in: "Vandemeulebroecke et al. (2018)"
<doi:10.1002/pst.1912>, "Vandemeulebroecke et al. (2019)"
<doi:10.1002/psp4.12455>, and "Morris et al. (2019)"
<doi:10.1136/bmjopen-2019-030215>.

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
