%global packname  snotelr
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Calculate and Visualize 'SNOTEL' Snow Data and Seasonality

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-wdman 
BuildRequires:    R-CRAN-RSelenium 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-wdman 
Requires:         R-CRAN-RSelenium 
Requires:         R-CRAN-memoise 

%description
Programmatic interface to the 'SNOTEL' snow data
(<https://www.wcc.nrcs.usda.gov/snow/>). Provides easy downloads of snow
data into your R work space or a local directory. Additional
post-processing routines to extract snow season indexes are provided.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
