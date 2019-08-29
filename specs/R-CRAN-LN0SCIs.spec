%global packname  LN0SCIs
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Simultaneous CIs for Ratios of Means of Log-Normal Populationswith Zeros

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Construct the simultaneous confidence intervals for ratios of means of
Log-normal populations with zeros. It also has a Python module that do the
same thing, and can be applied to multiple comparisons of parameters of
any k mixture distributions. And we provide four methods, the method based
on generalized pivotal quantity with order statistics and the quantity
based on Wilson by Li et al. (2009) <doi:10.1016/j.spl.2009.03.004>
(GPQW), and the methods based on generalized pivotal quantity with order
statistics and the quantity based on Hannig (2009)
<doi:10.1093/biomet/asp050> (GPQH). The other two methods are based on
two-step MOVER intervals by Amany H, Abdel K (2015)
<doi:10.1080/03610918.2013.767911>. We deduce Fiducial generalized pivotal
two-step MOVER intervals based on Wilson quantity (FMW) and based on
Hannig's quantity (FMWH). All these approach you can find in the paper of
us which it has been submitted.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
