%global packname  ideq
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Dynamic Spatio-Temporal Models, Including theIntegrodifference Equation Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rgen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-mvtnorm 

%description
In contrast to other methods of modeling spatio-temporal data, dynamic
spatio-temporal models (DSTMs) directly model the dynamic data-generating
process. 'ideq' supports two main classes of DSTMs: (1) empirical
orthogonal function (EOF) models and (2) integrodifference equation (IDE)
models. EOF models do not directly use any spatial information; instead,
they make use of observed relationships in the data (the principal
components) to model the underlying process. In contrast, IDE models are
based on diffusion dynamics and the process evolution is governed by a
(typically Gaussian) redistribution kernel. Both types have a variety of
options for specifying the model components, including the process matrix,
process error, and observation error. The classic reference for DSTMs is
Noel Cressie and Christopher K. Wikle (2011, ISBN:978-0471692744). For IDE
models specifically, see Christopher K. Wikle and Noel Cressie (1999,
<https://www.jstor.org/stable/2673587>) and Christopher K. Wikle (2002,
<doi:10.1191/1471082x02st036oa>).

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
