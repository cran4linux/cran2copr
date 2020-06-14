%global packname  CluMP
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          2%{?dist}
Summary:          Clustering of Micro Panel Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-NbClust >= 3.0
BuildRequires:    R-CRAN-amap >= 0.8.16
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-tableone 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-NbClust >= 3.0
Requires:         R-CRAN-amap >= 0.8.16
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-MASS 
Requires:         R-CRAN-tableone 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-data.table 

%description
Two-step feature-based clustering method designed for micro panel
(longitudinal) data with the artificial panel data generator. See Sobisek,
Stachova, Fojtik (2018) <arXiv:1807.05926>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
