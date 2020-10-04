%global packname  SiteAdapt
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Site Adaptation of Solar Irradiance Modeled Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmulti 
BuildRequires:    R-CRAN-solaR 
BuildRequires:    R-CRAN-hyfo 
BuildRequires:    R-CRAN-hydroGOF 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-stats 
Requires:         R-CRAN-glmulti 
Requires:         R-CRAN-solaR 
Requires:         R-CRAN-hyfo 
Requires:         R-CRAN-hydroGOF 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-stats 

%description
The SiteAdapt procedure improves the accuracy of modeled solar irradiance
series through site-adaptation with coincident ground-based measurements
relying on the use of a regression preprocessing followed by an empirical
quantile mapping (eQM) correction. Fernandez-Peruchena et al (2020)
<doi:10.3390/rs12132127>.

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
