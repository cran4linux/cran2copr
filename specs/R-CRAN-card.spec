%global __brp_check_rpaths %{nil}
%global packname  card
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cardiovascular and Autonomic Research Design

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lutz 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lutz 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-survival 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-generics 
Requires:         R-methods 
Requires:         R-CRAN-ggrepel 

%description
Tools that can aid in the assessment of the autonomic regulation of
cardiovascular physiology. The aims of this package are to: 1) study
electrocardiography (both intervals and morphology) as extensions of
signal processing, 2) study circadian rhythms and how it effects autonomic
physiology, 3) assess clinical risk of autonomic dysfunction on
cardiovascular health through the perspective of epidemiology and
causality. The analysis of circadian rhythms through cosinor analysis are
built upon the methods by Cornelissen (2014) <doi:10.1186/1742-4682-11-16>
and Refinetti, Cornelissen, Halberg (2014)
<doi:10.1080/09291010600903692>.

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
