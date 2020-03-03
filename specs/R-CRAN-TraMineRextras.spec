%global packname  TraMineRextras
%global packver   0.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.7
Release:          1%{?dist}
Summary:          TraMineR Extension

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-TraMineR >= 2.0.8
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-survival 
Requires:         R-CRAN-TraMineR >= 2.0.8
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-cluster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-survival 

%description
Collection of ancillary functions and utilities to be used in conjunction
with the 'TraMineR' package for sequence data exploration. Most of the
functions are in test phase, lack systematic consistency check of the
arguments and are subject to changes. Once fully checked, some of the
functions of this collection could be included in a next release of
'TraMineR'.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
