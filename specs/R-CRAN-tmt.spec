%global packname  tmt
%global packver   0.2.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1.0
Release:          3%{?dist}
Summary:          Estimation of the Rasch Model for Multistage Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Provides conditional maximum likelihood (CML) estimation of item
parameters in multistage designs (Zwitser & Maris, 2013,
<doi:10.1007/s11336-013-9369-6>) and CML estimation for conventional
designs. Additional features are the likelihood ratio test (Andersen,
1973, <doi:10.1007/BF02291180>) and simulation of multistage designs.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
