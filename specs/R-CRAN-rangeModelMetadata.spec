%global packname  rangeModelMetadata
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Provides Templates for Metadata Files Associated with SpeciesRange Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spocc 
BuildRequires:    R-CRAN-spThin 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-MASS 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spocc 
Requires:         R-CRAN-spThin 
Requires:         R-utils 

%description
Range Modeling Metadata Standards (RMMS) address three challenges: they
(i) are designed for convenience to encourage use, (ii) accommodate a wide
variety of applications, and (iii) are extensible to allow the community
of range modelers to steer it as needed. RMMS are based on a data
dictionary that specifies a hierarchical structure to catalog different
aspects of the range modeling process. The dictionary balances a
constrained, minimalist vocabulary to improve standardization with
flexibility for users to provide their own values. Merow et al. (2019)
<DOI:10.1111/geb.12993> describe the standards in more detail. Note that
users who prefer to use the R package 'ecospat' can obtain it from
<https://github.com/ecospat/ecospat>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
