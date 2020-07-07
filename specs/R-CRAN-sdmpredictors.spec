%global packname  sdmpredictors
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          3%{?dist}
Summary:          Species Distribution Modelling Predictor Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-R.utils >= 2.4.0
BuildRequires:    R-CRAN-rgdal >= 1.1.10
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-R.utils >= 2.4.0
Requires:         R-CRAN-rgdal >= 1.1.10
Requires:         R-stats 
Requires:         R-utils 

%description
Terrestrial and marine predictors for species distribution modelling from
multiple sources, including WorldClim <http://www.worldclim.org/>,,
ENVIREM <http://envirem.github.io/>, Bio-ORACLE <http://bio-oracle.org/>
and MARSPEC <http://www.marspec.org/>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
