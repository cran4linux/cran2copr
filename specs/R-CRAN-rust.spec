%global packname  rust
%global packver   1.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8
Release:          1%{?dist}
Summary:          Ratio-of-Uniforms Simulation with Transformation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-graphics 
Requires:         R-stats 

%description
Uses the generalized ratio-of-uniforms (RU) method to simulate from
univariate and (low-dimensional) multivariate continuous distributions.
The user specifies the log-density, up to an additive constant. The RU
algorithm is applied after relocation of mode of the density to zero, and
the user can choose a tuning parameter r. For details see Wakefield,
Gelfand and Smith (1991) <DOI:10.1007/BF01889987>, Efficient generation of
random variates via the ratio-of-uniforms method, Statistics and Computing
(1991) 1, 129-133.  A Box-Cox variable transformation can be used to make
the input density suitable for the RU method and to improve efficiency.
In the multivariate case rotation of axes can also be used to improve
efficiency. From version 1.2.0 the 'Rcpp' package
<https://cran.r-project.org/package=Rcpp> can be used to improve
efficiency.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
