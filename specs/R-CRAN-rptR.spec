%global packname  rptR
%global packver   0.9.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.22
Release:          3%{?dist}
Summary:          Repeatability Estimation for Gaussian and Non-Gaussian Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.1.2
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-parallel >= 3.1.2
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-pbapply 

%description
Estimating repeatability (intra-class correlation) from Gaussian, binary,
proportion and Poisson data.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
