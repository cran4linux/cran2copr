%global __brp_check_rpaths %{nil}
%global packname  NitrogenUptake2016
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Data and Source Code From: Nitrogen Uptake and AllocationEstimates for Spartina Alterniflora and Distichlis Spicata

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-MASS 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-car 
Requires:         R-MASS 

%description
Contains data, code, and figures from Hill et al. 2018a (Journal of
Experimental Marine Biology and Ecology; <DOI:
10.1016/j.jembe.2018.07.006>) and Hill et al. 2018b (Data In Brief <DOI:
10.1016/j.dib.2018.09.133>). Datasets document plant allometry, stem
heights, nutrient and stable isotope content, and sediment denitrification
enzyme assays. The data and analysis offer an examination of nitrogen
uptake and allocation in two salt marsh plant species.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
