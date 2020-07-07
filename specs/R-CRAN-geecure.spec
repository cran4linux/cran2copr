%global packname  geecure
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}
Summary:          Marginal Proportional Hazards Mixture Cure Models withGeneralized Estimating Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-methods 
Requires:         R-survival 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-geepack 
Requires:         R-methods 

%description
Features the marginal parametric and semi-parametric proportional hazards
mixture cure models for analyzing clustered survival data with a possible
cure fraction. A reference is Yi Niu and Yingwei Peng (2014)
<doi:10.1016/j.jmva.2013.09.003>.

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
