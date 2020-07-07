%global packname  spBayes
%global packver   0.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          3%{?dist}
Summary:          Univariate and Multivariate Spatial-Temporal Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-Formula 
Requires:         R-Matrix 

%description
Fits univariate and multivariate spatio-temporal random effects models for
point-referenced data using Markov chain Monte Carlo (MCMC). Details are
given in Finley, Banerjee, and Gelfand (2015) <doi:10.18637/jss.v063.i13>
and Finley, Banerjee, and Cook (2014) <doi:10.1111/2041-210X.12189>.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NOTES
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
