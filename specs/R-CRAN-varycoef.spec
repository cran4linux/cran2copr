%global packname  varycoef
%global packver   0.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          2%{?dist}
Summary:          Modeling Spatially Varying Coefficients

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-optimParallel >= 0.8
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-optimParallel >= 0.8
Requires:         R-CRAN-spam 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-sp 

%description
Implements a maximum likelihood estimation (MLE) method for estimation and
prediction in spatially varying coefficient (SVC) models (Dambon et al.
(2020) <arXiv:2001.08089>). Covariance tapering (Furrer et al. (2006)
<doi:10.1198/106186006X132178>) can be applied such that the method scales
to large data.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
