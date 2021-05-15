%global packname  gfer
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Green Finance and Environmental Risk

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scatterpie 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-googlesheets 
BuildRequires:    R-CRAN-gsheet 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scatterpie 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-googlesheets 
Requires:         R-CRAN-gsheet 

%description
Focuses on data collecting, analyzing and visualization in green finance
and environmental risk research and analysis. Main function includes
environmental data collecting from official websites such as MEP (Ministry
of Environmental Protection of China, <https://www.mee.gov.cn>), water
related projects identification and environmental data visualization.

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
