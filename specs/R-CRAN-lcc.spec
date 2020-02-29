%global debug_package %{nil}
%global packname  lcc
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Longitudinal Concordance Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-nlme >= 3.1.124
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-hnp 
BuildRequires:    R-CRAN-gdata 
Requires:         R-nlme >= 3.1.124
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-hnp 
Requires:         R-CRAN-gdata 

%description
Estimates the longitudinal concordance correlation to access the
longitudinal agreement profile. The estimation approach implemented is
variance components approach based on polynomial mixed effects regression
model, as proposed by Oliveira, Hinde and Zocchi (2018)
<doi:10.1007/s13253-018-0321-1>.  In addition, non-parametric confidence
intervals were implemented using percentile method or normal-approximation
based on Fisher Z-transformation.

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
