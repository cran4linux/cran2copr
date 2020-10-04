%global packname  zoon
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          3%{?dist}%{?buildtag}
Summary:          Reproducible, Accessible & Shareable Species DistributionModelling

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.4.20
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rfigshare 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-raster >= 2.4.20
Requires:         R-CRAN-dismo 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rfigshare 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-rworldmap 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-testthat 

%description
Reproducible and remixable species distribution modelling. The package
reads user submitted modules from an online repository, runs full species
distribution modelling workflows and returns output that is fully
reproducible. For examples and detailed discussion refer to: N.Golding et
al. (2017) 'The zoon r package for reproducible and shareable species
distribution modelling'. Methods in Ecology and Evolution.
<doi:10.1111/2041-210X.12858>. The package 'SDMTools' is used for testing
and, though this package is archived, you can access it here if needed,
<https://cran.r-project.org/src/contrib/Archive/SDMTools/>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
