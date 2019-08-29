%global packname  eco
%global packver   4.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          1%{?dist}
Summary:          Ecological Inference in 2x2 Tables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
Requires:         R-MASS 
Requires:         R-utils 

%description
Implements the Bayesian and likelihood methods proposed in Imai, Lu, and
Strauss (2008 <DOI: 10.1093/pan/mpm017>) and (2011
<DOI:10.18637/jss.v042.i05>) for ecological inference in 2 by 2 tables as
well as the method of bounds introduced by Duncan and Davis (1953).  The
package fits both parametric and nonparametric models using either the
Expectation-Maximization algorithms (for likelihood models) or the Markov
chain Monte Carlo algorithms (for Bayesian models).  For all models, the
individual-level data can be directly incorporated into the estimation
whenever such data are available. Along with in-sample and out-of-sample
predictions, the package also provides a functionality which allows one to
quantify the effect of data aggregation on parameter estimation and
hypothesis testing under the parametric likelihood models.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
