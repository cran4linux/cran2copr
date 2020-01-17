%global packname  Numero
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Statistical Framework to Define Subgroups in Complex Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-Rcpp >= 0.11.4

%description
High-dimensional datasets that do not exhibit a clear intrinsic clustered
structure pose a challenge to conventional clustering algorithms. For this
reason, we developed an unsupervised framework that helps scientists to
better subgroup their datasets based on visual cues, please see Gao S,
Mutter S, Casey A, Makinen V-P (2019) Numero: a statistical framework to
define multivariable subgroups in complex population-based datasets, Int J
Epidemiology, 48:369-37, <doi:10.1093/ije/dyy113>. The framework includes
the necessary functions to construct a self-organizing map of the data, to
evaluate the statistical significance of the observed data patterns, and
to visualize the results.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/extcode
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
