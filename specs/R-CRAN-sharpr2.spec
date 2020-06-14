%global packname  sharpr2
%global packver   1.1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1.0
Release:          2%{?dist}
Summary:          Estimating Regulatory Scores and Identifying ATAC-STARR Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-mvtnorm >= 1.0
BuildRequires:    R-methods 
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-mvtnorm >= 1.0
Requires:         R-methods 

%description
An algorithm for identifying high-resolution driver elements for datasets
from a high-definition reporter assay library. Xinchen Wang, Liang He,
Sarah Goggin, Alham Saadat, Li Wang, Melina Claussnitzer, Manolis Kellis
(2017) <doi:10.1101/193136>.

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
%{rlibdir}/%{packname}/INDEX
