%global packname  lognorm
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for the Lognormal Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
Requires:         R-Matrix 

%description
The lognormal distribution (Limpert et al. (2001)
<doi:10.1641/0006-3568(2001)051%5B0341:lndats%5D2.0.co;2>) can
characterize uncertainty that is bounded by zero. This package provides
estimation of distribution parameters, computation of moments and other
basic statistics, and an approximation of the distribution of the sum of
several correlated lognormally distributed variables (Lo 2013
<doi:10.12988/ams.2013.39511>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/docu
%doc %{rlibdir}/%{packname}/genData
%{rlibdir}/%{packname}/INDEX
