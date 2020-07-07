%global packname  alphaOutlier
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Obtain Alpha-Outlier Regions for Well-Known ProbabilityDistributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-quantreg 
Requires:         R-graphics 
Requires:         R-stats 

%description
Given the parameters of a distribution, the package uses the concept of
alpha-outliers by Davies and Gather (1993) to flag outliers in a data set.
See Davies, L.; Gather, U. (1993): The identification of multiple
outliers, JASA, 88 423, 782-792, <doi:10.1080/01621459.1993.10476339> for
details.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
