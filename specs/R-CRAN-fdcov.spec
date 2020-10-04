%global packname  fdcov
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Covariance Operators

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-corrplot 
Requires:         R-stats 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-corrplot 

%description
Provides a variety of tools for the analysis of covariance operators
including k-sample tests for equality and classification and clustering
methods found in the works of Cabassi et al (2017)
<doi:10.1214/17-EJS1347>, Kashlak et al (2017) <arXiv:1604.06310>, Pigoli
et al (2014) <doi:10.1093/biomet/asu008>, and Panaretos et al (2010)
<doi:10.1198/jasa.2010.tm09239>.

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
