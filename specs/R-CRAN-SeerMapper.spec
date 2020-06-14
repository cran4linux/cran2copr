%global packname  SeerMapper
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          2%{?dist}
Summary:          A Quick Way to Map U.S. Rates and Data of U.S. States, Counties,Census Tracts, or Seer Registries using 2000 and 2010 U.S.Census Boundaries

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
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
Requires:         R-methods 
Requires:         R-CRAN-SeerMapperRegs 
Requires:         R-CRAN-SeerMapperEast 
Requires:         R-CRAN-SeerMapperWest 
Requires:         R-CRAN-SeerMapper2010Regs 
Requires:         R-CRAN-SeerMapper2010East 
Requires:         R-CRAN-SeerMapper2010West 

%description
Provides an easy way to map seer registry area rate data on a U.S. map.
The U.S. data may be mapped at the state or state/county. U.S. Seer
registry data may be mapped at the Seer registry area, Seer Registry
area/county or Seer Registry area/county/census tract level. The function
uses a calculated default categorization breakpoint list for 5 categories,
when not breakpoint list is provided or the number of categories is
specified by the user. A user provided break point list is limited to
containing 5 values. The number of calculated categories may be from 3 to
11. The user provide the p-value for each area and request hatching over
any areas with a p-value > 0.05. Other types of comparisons can be
specified.  If states or state/counties are used, the area identifier is
the U.S. FIPS codes for states and counties, 2 digits and 5 digits
respectfully.  If the data is for U.S. Seer Registry areas, the Seer
Registry area identifier used to link the data to the geographical area is
a Seer Registry area abbreviation.  See documentation for the list of
acceptable Seer Registry area names and abbreviations. The state
boundaries are overlaid all rate maps. The package contains the boundary
data for state, county, Seer Registry areas, and census tracts for
counties within a Seer registry area. The package support boundary data
from the 2000 and 2010 U.S. Census. The SeerMapper package version
contains the U.S. Census 2000 and 2010 boundary data for the regional,
state, Seer Registry, and county levels.  Six supplement packages contain
the census tract boundary data. Copyrighted 2014, 2015, 2016, 2017, 2018
and 2019 by Pearson and Pickle.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
