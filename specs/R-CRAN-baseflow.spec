%global packname  baseflow
%global packver   0.11.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.2
Release:          1%{?dist}
Summary:          Computes Hydrograph Separation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-airGR 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-airGR 

%description
Computes hydrograph separation using the conceptual automated process from
Pelletier and Andreassian (2019) <doi:10.5194/hess-2019-503>. Contains
scalar and vectorized functions to compute correlation criterion to
calibrate the baseflow separation model.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
