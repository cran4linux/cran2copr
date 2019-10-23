%global packname  KnowBR
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Discriminating Well Surveyed Spatial Units from ExhaustiveBiodiversity Databases

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fossil 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-fossil 
Requires:         R-mgcv 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-vegan 

%description
It uses species accumulation curves and diverse estimators to assess, at
the same time, the levels of survey coverage in multiple geographic cells
of a size defined by the user or polygons. It also enables the
geographical depiction of observed species richness, survey effort and
completeness values including a background with administrative areas.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
