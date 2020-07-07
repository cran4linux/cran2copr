%global packname  AHMbook
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Functions and Data for the Book "Applied Hierarchical Modelingin Ecology" Vols 1 and 2

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-unmarked >= 0.12.2
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-unmarked >= 0.12.2
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-spdep 

%description
Provides functions and data sets to accompany the two volume publication
"Applied Hierarchical Modeling in Ecology: Analysis of distribution,
abundance and species richness in R and BUGS" by Marc Kéry and Andy Royle:
volume 1 (2016, ISBN: 978-0-12-801378-6) and volume 2 (2020, ISBN:
978-0-12-809585-0),
<https://www.mbr-pwrc.usgs.gov/pubanalysis/keryroylebook>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
