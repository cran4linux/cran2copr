%global packname  BasketballAnalyzeR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          Analysis and Visualization of Basketball Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-CRAN-statnet.common >= 4.2
BuildRequires:    R-CRAN-directlabels >= 2018.05
BuildRequires:    R-CRAN-PBSmapping >= 2.70
BuildRequires:    R-CRAN-sna >= 2.4
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-dendextend >= 1.8
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-GGally >= 1.4
BuildRequires:    R-CRAN-sp >= 1.3
BuildRequires:    R-CRAN-stringr >= 1.3
BuildRequires:    R-CRAN-readr >= 1.3
BuildRequires:    R-CRAN-hexbin >= 1.27
BuildRequires:    R-CRAN-network >= 1.13.0
BuildRequires:    R-CRAN-scales >= 1.0
BuildRequires:    R-CRAN-corrplot >= 0.80
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-ggrepel >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-ggnetwork >= 0.5
BuildRequires:    R-CRAN-rlang >= 0.4.3
BuildRequires:    R-CRAN-circlize >= 0.4
BuildRequires:    R-CRAN-operators >= 0.1
BuildRequires:    R-CRAN-ggplotify >= 0.0.3
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-MASS >= 7.3
Requires:         R-CRAN-statnet.common >= 4.2
Requires:         R-CRAN-directlabels >= 2018.05
Requires:         R-CRAN-PBSmapping >= 2.70
Requires:         R-CRAN-sna >= 2.4
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-dendextend >= 1.8
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-GGally >= 1.4
Requires:         R-CRAN-sp >= 1.3
Requires:         R-CRAN-stringr >= 1.3
Requires:         R-CRAN-readr >= 1.3
Requires:         R-CRAN-hexbin >= 1.27
Requires:         R-CRAN-network >= 1.13.0
Requires:         R-CRAN-scales >= 1.0
Requires:         R-CRAN-corrplot >= 0.80
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-ggrepel >= 0.8
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-ggnetwork >= 0.5
Requires:         R-CRAN-rlang >= 0.4.3
Requires:         R-CRAN-circlize >= 0.4
Requires:         R-CRAN-operators >= 0.1
Requires:         R-CRAN-ggplotify >= 0.0.3
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Contains data and code to accompany the book P. Zuccolotto and M. Manisera
(2020) Basketball Data Science. Applications with R. CRC Press. ISBN
9781138600799.

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
