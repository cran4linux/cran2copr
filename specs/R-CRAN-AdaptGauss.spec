%global packname  AdaptGauss
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}
Summary:          Gaussian Mixture Models (GMM)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DataVisualizations 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-pracma 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DataVisualizations 

%description
Multimodal distributions can be modelled as a mixture of components. The
model is derived using the Pareto Density Estimation (PDE) for an
estimation of the pdf. PDE has been designed in particular to identify
groups/classes in a dataset. Precise limits for the classes can be
calculated using the theorem of Bayes. Verification of the model is
possible by QQ plot, Chi-squared test and Kolmogorov-Smirnov test. The
package is based on the publication of Ultsch, A., Thrun, M.C.,
Hansen-Goos, O., Lotsch, J. (2015) <DOI:10.3390/ijms161025897>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
