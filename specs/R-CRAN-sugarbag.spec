%global packname  sugarbag
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Create Tessellated Hexagon Maps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-tidyr >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-sf >= 0.7
BuildRequires:    R-CRAN-rmapshaper >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-lwgeom >= 0.1.7
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-geosphere >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-tidyr >= 0.8
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-sf >= 0.7
Requires:         R-CRAN-rmapshaper >= 0.4.1
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-lwgeom >= 0.1.7
Requires:         R-CRAN-rlang 

%description
Create a hexagon tilegram from spatial polygons. Each polygon is
represented by a hexagon tile, placed as close to it's original centroid
as possible, with a focus on maintaining spatial relationship to a focal
point. Developed to aid visualisation and analysis of spatial
distributions across Australia, which can be challenging due to the
concentration of the population on the coast and wide open interior.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
