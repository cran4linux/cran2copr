%global packname  coefficientalpha
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Robust Coefficient Alpha and Omega with Missing and Non-NormalData

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rsem 
BuildRequires:    R-CRAN-lavaan 
Requires:         R-CRAN-rsem 
Requires:         R-CRAN-lavaan 

%description
Cronbach's alpha and McDonald's omega are widely used reliability or
internal consistency measures in social, behavioral and education
sciences. Alpha is reported in nearly every study that involves measuring
a construct through multiple test items. The package 'coefficientalpha'
calculates coefficient alpha and coefficient omega with missing data and
non-normal data. Robust standard errors and confidence intervals are also
provided. A test is also available to test the tau-equivalent and
homogeneous assumptions. Version 0.5 added the bootstrap confidence
intervals.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
