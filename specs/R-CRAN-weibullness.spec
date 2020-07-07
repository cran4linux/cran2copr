%global packname  weibullness
%global packver   1.19.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.19.8
Release:          3%{?dist}
Summary:          Goodness-of-Fit Test for Weibull Distribution (Weibullness)

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
Performs a goodness-of-fit test of Weibull distribution (weibullness test)
and provides the maximum likelihood estimates of the three-parameter
Weibull distribution. Note that the threshold parameter is estimated based
on the correlation from the Weibull plot. For more details, see Park
(2018) <doi:10.1155/2018/6056975>. This work was supported by the National
Research Foundation of Korea (NRF) grant funded by the Korea government
(No. NRF-2017R1A2B4004169).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
