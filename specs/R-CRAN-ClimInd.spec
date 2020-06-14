%global packname  ClimInd
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Climate Indices

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-SPEI 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-weathermetrics 
Requires:         R-CRAN-SPEI 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-weathermetrics 

%description
Computes 138 standard climate indices at monthly, seasonal and annual
resolution. These indices were selected, based on their direct and
significant impacts on target sectors, after a thorough review of the
literature in the field of extreme weather events and natural hazards.
Overall, the selected indices characterize different aspects of the
frequency, intensity and duration of extreme events, and are derived from
a broad set of climatic variables, including surface air temperature,
precipitation, relative humidity, wind speed, cloudiness, solar radiation,
and snow cover. The 138 indices have been classified as follow:
Temperature based indices (42), Precipitation based indices (22),
Bioclimatic indices (21), Wind-based indices (5), Aridity/ continentality
indices (10), Snow-based indices (13), Cloud/radiation based indices (6),
Drought indices (8), Fire indices (5), Tourism indices (5).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
