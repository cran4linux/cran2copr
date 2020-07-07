%global packname  FlexScan
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Flexible Scan Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-smerc 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-smerc 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spdep 
Requires:         R-methods 
Requires:         R-graphics 

%description
An easy way to conduct flexible scan. Monte-Carlo method is used to test
the spatial clusters given the cases, population, and shapefile. A table
with formal style and a map with clusters are included in the result
report. The method can be referenced at: Toshiro Tango and Kunihiko
Takahashi (2005) <doi:10.1186/1476-072X-4-11>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
