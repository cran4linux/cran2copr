%global packname  MNP
%global packver   3.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}
Summary:          R Package for Fitting the Multinomial Probit Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1
Requires:         R-core >= 2.1
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
Requires:         R-MASS 
Requires:         R-utils 

%description
Fits the Bayesian multinomial probit model via Markov chain Monte Carlo.
The multinomial probit model is often used to analyze the discrete choices
made by individuals recorded in survey data. Examples where the
multinomial probit model may be useful include the analysis of product
choice by consumers in market research and the analysis of candidate or
party choice by voters in electoral studies. The MNP package can also fit
the model with different choice sets for each individual, and complete or
partial individual choice orderings of the available alternatives from the
choice set. The estimation is based on the efficient marginal data
augmentation algorithm that is developed by Imai and van Dyk (2005). ``A
Bayesian Analysis of the Multinomial Probit Model Using the Data
Augmentation,'' Journal of Econometrics, Vol. 124, No. 2 (February), pp.
311-334. <DOI:10.1016/j.jeconom.2004.02.002> Detailed examples are given
in Imai and van Dyk (2005). ``MNP: R Package for Fitting the Multinomial
Probit Model.'' Journal of Statistical Software, Vol. 14, No. 3 (May), pp.
1-32. <DOI:10.18637/jss.v014.i03>.

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
