%global packname  cubfits
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Codon Usage Bias Fits

License:          Mozilla Public License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Estimating mutation and selection coefficients on synonymous codon bias
usage based on models of ribosome overhead cost (ROC). Multinomial
logistic regression and Markov Chain Monte Carlo are used to estimate and
predict protein production rates with/without the presence of expressions
and measurement errors. Work flows with examples for simulation,
estimation and prediction processes are also provided with parallelization
speedup. The whole framework is tested with yeast genome and gene
expression data of Yassour, et al. (2009) <doi:10.1073/pnas.0812841106>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/ex_data
%doc %{rlibdir}/%{packname}/workflow
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
