%global packname  psychNET
%global packver   0.0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4.1
Release:          1%{?dist}
Summary:          Psychometric Networks for Intensive Longitudinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-SparseTSCGM 
BuildRequires:    R-CRAN-mlVAR 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-graphicalVAR 
BuildRequires:    R-CRAN-bigtime 
BuildRequires:    R-CRAN-mgm 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-longitudinal 
BuildRequires:    R-CRAN-networktools 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ordinalNet 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-picasso 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-imputeTS 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-SparseTSCGM 
Requires:         R-CRAN-mlVAR 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-graphicalVAR 
Requires:         R-CRAN-bigtime 
Requires:         R-CRAN-mgm 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-longitudinal 
Requires:         R-CRAN-networktools 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-car 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-ordinalNet 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-ncvreg 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-picasso 
Requires:         R-CRAN-corpcor 

%description
In the past decade, mental processes have been conceptualized as complex
networks of interacting psychiatric symptoms. These networks that can be
visualized by means of conditional independence graphs. For estimating the
underlying directed graph from intensive longitudinal data, vector
autoregression (VAR) is the most commonly used tool. This package wraps
several methods in the VAR family that can be used to estimate conditional
independence graphs (networks) from multivariate time-series data. The
package can fit the simple VAR and VAR with exogenous variables (VARX)
model Lutkepohl, H. (2005) <doi:10.1007/978-3-540-27752-1> that are
currently available from the R package 'vars', and its sparse alternative
by Basu S. and Michailidis, G.(2015) <doi:10.1214/15-AOS1315> and sparse
vector error correction model (SVECM) implemented in the R package
'sparsevar'. The sparse graphical VAR with covariance estimation by Wild,
B., Eichler, M., Friederich, H. C., Hartmann, M., Zipfel, S., & Herzog, W.
(2010) <doi:10.1186/1471-2288-10-28> from the R package 'graphicalVAR' and
the dynamic factor model (DFM) by Doz, Gianone & Reichlin (2011)
<doi:10.1016/j.jeconom.2011.02.012> from the R package 'dynfactoR' are
also available. Sparse estimation of high dimensional VAR, VARX, and
vector autoregressive moving average (VARMA) and models using hierarchical
lag structures Nicholson, W. B., Bien, J., Matteson, D. S. (2017)
<arXiv:1412.5250v3> implemented from the R package 'bigtime' and mixed VAR
for symptom time series with marginal distributions in the exponential
family Haslbeck, J., Waldorp, L. J. (2015) <arXiv:1510.06871> from the
package 'mgm' can also be used with this package. For the inference of
symptom networks from multivariate time series of multiple individuals the
'psychNET' package adopts the multi-level VAR (MLVAR) by Epskamp, S.,
Waldorp, L. J., Mottus, R., & Borsboom, D. (2017) <arXiv:1609.04156v6>
implemented in the R package 'mlVAR' and for the high-dimensional setting
the sparse time series chain graphical model by Abegaz, F., Wit, E. (2013)
<doi:10.1093/biostatistics/kxt005> available from the R package
'sparseTSCGM'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
