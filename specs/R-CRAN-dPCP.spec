%global __brp_check_rpaths %{nil}
%global packname  dPCP
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Analysis of Multiplex Digital PCR Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-exactci 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-exactci 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-graphics 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
The automated clustering and quantification of the digital PCR data is
based on the combination of 'DBSCAN' (Hahsler et al. (2019)
<doi:10.18637/jss.v091.i01>) and 'c-means' (Bezdek et l. (1981)
<doi:10.1007/978-1-4757-0450-1>) algorithms. The analysis is independent
of multiplexing geometry, dPCR system, and input amount. The details about
input data and parameters are available in the vignette.

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
