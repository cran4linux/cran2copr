%global packname  geospacom
%global packver   0.5-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          1%{?dist}
Summary:          Facilitate Generating of Distance Matrices Used in Package'spacom' and Plotting Data on Maps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-geosphere 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-geosphere 

%description
Generates distance matrices from shape files and represents spatially
weighted multilevel analysis results (see 'spacom')

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
