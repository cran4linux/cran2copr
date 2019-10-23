%global packname  generalCorr
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Generalized Correlations and Plausible Causal Paths

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable >= 1.8
BuildRequires:    R-CRAN-meboot >= 1.4
BuildRequires:    R-CRAN-np >= 0.60
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-lattice 
Requires:         R-CRAN-xtable >= 1.8
Requires:         R-CRAN-meboot >= 1.4
Requires:         R-CRAN-np >= 0.60
Requires:         R-CRAN-psych 
Requires:         R-lattice 

%description
Since causal paths from data are important for all sciences, the package
provides many sophisticated functions. causeSummary() gives
easy-to-interpret causal paths.  Let Z denote control variables and
compare two flipped kernel regressions: X=f(Y, Z)+e1 and Y=g(X,Z)+e2. Our
criterion Cr1 says that if |e1*Y|>|e2*X| then variation in X is more
"exogenous or independent" than in Y and causal path is X to Y. Criterion
Cr2 requires |e2|<|e1|. These inequalities between many absolute value are
quantified by four orders of stochastic dominance. Our third criterion Cr3
for the causal path X to Y requires new generalized partial correlations
to satisfy |r*(x|y,z)|< |r*(y|x,z)|. The function parcorMany() reports
generalized partials between the first variable and all others.  The
package provides additional R tools for causal assessment, "outlier
detection," and for numerical integration by the trapezoidal rule,
stochastic dominance, pillar 3D charts, etc. We also provide functions for
bootstrap-based statistical inference for causal paths.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
