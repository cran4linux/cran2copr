%global packname  JMcmprsk
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          2%{?dist}
Summary:          Joint Models for Longitudinal and Competing Risks Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-Rcpp 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-statmod 

%description
Fit joint models of continuous or ordinal longitudinal data and
time-to-event data with competing risks. For a detailed information, see
Robert Elashoff, Gang Li and Ning Li (2016, ISBN:9781439807828); Robert M.
Elashoff,Gang Li and Ning Li (2008) <doi:10.1111/j.1541-0420.2007.00952.x>
; Ning Li, Robert Elashoff, Gang Li and Jeffrey Saver (2010)
<doi:10.1002/sim.3798> .

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
