%global packname  Bayesrel
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Bayesian Reliability Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-Rcsdp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-Rcsdp 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Rdpack 

%description
So far, it provides the most common single test reliability estimates,
being: Coefficient Alpha, Guttman's lambda-2/-4/-6, greatest lower bound
and Mcdonald's Omega. The Bayesian estimates are provided with credible
intervals. The method for the Bayesian estimates, except for omega, is
sampling from the posterior inverse Wishart for the covariance matrix
based measures. See Murphy (2007)
<https://www.seas.harvard.edu/courses/cs281/papers/murphy-2007.pdf>. Gibbs
Sampling from the joint conditional distributions of a single factor model
in the case of omega. See Lee (2007, ISBN:978-0-470-02424-9). Methods for
the glb are from Moltner and Revelle (2018)
<https://www.rdocumentation.org/packages/psych/versions/1.8.10/topics/glb.algebraic>;
lambda-4 is from Benton (2015) <doi:10.1007/978-3-319-07503-7_19>; the
principal factor analysis is from Schlegel (2017)
<https://www.r-bloggers.com/iterated-principal-factor-method-of-factor-analysis-with-r/>;
and the analytic alpha interval is from Bonnett and Wright (2014)
<doi:10.1002/job.1960>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
