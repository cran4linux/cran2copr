%global packname  ClimMobTools
%global packver   0.2-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}
Summary:          Tools for Crowdsourcing Citizen Science in Agriculture

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-PlackettLuce >= 0.2.8
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nasapower 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-PlackettLuce >= 0.2.8
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-nasapower 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Toolkit for the 'ClimMob' platform in R. 'ClimMob' is an open source
software for crowdsourcing citizen science in agriculture
<https://climmob.net/climmob3/>. Developed by van Etten et al. (2019)
<doi:10.1017/S0014479716000739>, it turns the research paradigm on its
head; instead of a few researchers designing complicated trials to compare
several technologies in search of the best solutions, it enables many
farmers to carry out reasonably simple experiments that taken together can
offer even more information. 'ClimMobTools' enables project managers to
deep explore and analyse their 'ClimMob' data in R.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
