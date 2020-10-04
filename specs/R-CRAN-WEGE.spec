%global packname  WEGE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          A Metric to Rank Locations for Biodiversity Conservation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-stats 
Requires:         R-utils 

%description
Calculates the WEGE (Weighted Endemism including Global Endangerment
index) index for a particular area. Additionally it also calculates
rasters of KBA's (Key Biodiversity Area) criteria (A1a, A1b, A1e, and B1),
Weighted endemism (WE), the EDGE (Evolutionarily Distinct and Globally
Endangered) score, Evolutionary Distinctiveness (ED) and Extinction risk
(ER). Farooq, H., Azevedo, J., Belluardo F., Nanvonamuquitxo, C., Bennett,
D., Moat, J., Soares, A., Faurby, S. & Antonelli, A. (2020)
<doi:10.1101/2020.01.17.910299>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
