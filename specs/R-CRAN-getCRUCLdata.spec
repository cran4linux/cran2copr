%global packname  getCRUCLdata
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          'CRU' 'CL' v. 2.0 Climatology Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hoardr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Provides functions that automate downloading and importing University of
East Anglia Climate Research Unit ('CRU') 'CL' v. 2.0 climatology data,
facilitates the calculation of minimum temperature and maximum temperature
and formats the data into a tidy data frame as a 'tibble' or a list of
'raster' 'stack' objects for use.  'CRU' 'CL' v. 2.0 data are a gridded
climatology of 1961-1990 monthly means released in 2002 and cover all land
areas (excluding Antarctica) at 10 arcminutes (0.1666667 degree)
resolution.  For more information see the description of the data provided
by the University of East Anglia Climate Research Unit,
<https://crudata.uea.ac.uk/cru/data/hrg/tmc/readme.txt>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/paper
%{rlibdir}/%{packname}/INDEX
