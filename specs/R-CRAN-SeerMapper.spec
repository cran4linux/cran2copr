%global packname  SeerMapper
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          A Quick Way to Map U.S. Rates and Data of U. S. States,Counties, Census Tracts, or Seer Registries using 2000 and 2010U. S. Census Boundaries

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-SeerMapperRegs 
BuildRequires:    R-CRAN-SeerMapperEast 
BuildRequires:    R-CRAN-SeerMapperWest 
BuildRequires:    R-CRAN-SeerMapper2010Regs 
BuildRequires:    R-CRAN-SeerMapper2010East 
BuildRequires:    R-CRAN-SeerMapper2010West 
Requires:         R-graphics 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-SeerMapperRegs 
Requires:         R-CRAN-SeerMapperEast 
Requires:         R-CRAN-SeerMapperWest 
Requires:         R-CRAN-SeerMapper2010Regs 
Requires:         R-CRAN-SeerMapper2010East 
Requires:         R-CRAN-SeerMapper2010West 

%description
Provides an easy way to map seer registry area rate data on a U. S, map.
The U. S. data may be mapped at the state, U. S. NCI Seer Register,
state/county or census tract level. The function can categorize the data
into "n" quantiles, where "n" is 3 to 11 or the caller can specify a cut
point list for the categorizes. The caller can also provide the data and
the comparison operation to request hatching over any areas.  The default
operation and value are > 0.05 (p-values). The location id provided in the
data determines the geographic level of the mapping. If states,
state/counties or census tracts are being mapped, the location ids used
must be the U.S. FIPS codes for states (2 digits), state/counties (5
digits) or state/county/census tracts (11 digits). If the location id
references the U.S. Seer Registry areas, the Seer Registry area identifier
used to link the data to the geographical areas, then the location id is
the Seer Registry name or abbreviation. Additional parameters are used to
provide control over the drawing of the boundaries at the data's boundary
level and higher levels. The package uses modified boundary data from the
2000 and 2010 U. S. Census to reduce the storage requirements and improve
drawing speed. The 'SeerMapper' package contains the U. S. Census 2000 and
2010 boundary data for the regional, state, Seer Registry, and county
levels.  Six supplement packages contain the census tract boundary data
(see manual for more details.)

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
