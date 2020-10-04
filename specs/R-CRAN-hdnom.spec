%global packname  hdnom
%global packver   6.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Benchmarking and Visualization Toolkit for Penalized Cox Models

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-survAUC 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-survAUC 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Creates nomogram visualizations for penalized Cox regression models, with
the support of reproducible survival model building, validation,
calibration, and comparison for high-dimensional data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
