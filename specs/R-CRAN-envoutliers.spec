%global packname  envoutliers
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Methods for Identification of Outliers in Environmental Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-ecp 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-lokern 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-car 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-ecp 
Requires:         R-graphics 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-lokern 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 

%description
Three semi-parametric methods for detection of outliers in environmental
data based on kernel regression and subsequent analysis of smoothing
residuals. The first method (Campulova, Michalek, Mikuska and Bokal (2018)
<DOI: 10.1002/cem.2997>) analyzes the residuals using changepoint
analysis, the second method is based on control charts (Campulova, Veselik
and Michalek (2017) <DOI: 10.1016/j.apr.2017.01.004>) and the third method
(Holesovsky, Campulova and Michalek (2018) <DOI:
10.1016/j.apr.2017.06.005>) analyzes the residuals using extreme value
theory (Holesovsky, Campulova and Michalek (2018) <DOI:
10.1016/j.apr.2017.06.005>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
