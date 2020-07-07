%global packname  MSCMT
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          3%{?dist}
Summary:          Multivariate Synthetic Control Method Using Time Series

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-Rdpack 

%description
Three generalizations of the synthetic control method (which has already
an implementation in package 'Synth') are implemented: first, 'MSCMT'
allows for using multiple outcome variables, second, time series can be
supplied as economic predictors, and third, a well-defined
cross-validation approach can be used. Much effort has been taken to make
the implementation as stable as possible (including edge cases) without
losing computational efficiency. A detailed description of the main
algorithms is given in Becker and Klößner (2018)
<doi:10.1016/j.ecosta.2017.08.002>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
