%global packname  depend.truncation
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}
Summary:          Statistical Methods for the Analysis of Dependently TruncatedData

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
Estimation and testing methods for dependently truncated data.
Semi-parametric methods are based on Emura et al. (2011)<Stat Sinica
21:349-67>, Emura & Wang (2012)<doi:10.1016/j.jmva.2012.03.012>, and Emura
& Murotani (2015)<doi:10.1007/s11749-015-0432-8>. Parametric approaches
are based on Emura & Konno (2012)<doi:10.1007/s00362-014-0626-2> and Emura
& Pan (2017)<doi:10.1007/s00362-017-0947-z>. A regression approach is
based on Emura & Wang (2016)<doi:10.1007/s10463-015-0526-9>.
Quasi-independence tests are based on Emura & Wang
(2010)<doi:10.1016/j.jmva.2009.07.006>. Right-truncated data for Japanese
male centenarians are given by Emura & Murotani
(2015)<doi:10.1007/s11749-015-0432-8>.

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
