%global packname  whitening
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Whitening and High-Dimensional Canonical Correlation Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.9
BuildRequires:    R-stats 
Requires:         R-CRAN-corpcor >= 1.6.9
Requires:         R-stats 

%description
Implements the whitening methods (ZCA, PCA, Cholesky, ZCA-cor, and
PCA-cor) discussed in Kessy, Lewin, and Strimmer (2018) "Optimal whitening
and decorrelation", <doi:10.1080/00031305.2016.1277159>, as well as the
whitening approach to canonical correlation analysis allowing negative
canonical correlations described in Jendoubi and Strimmer (2019) "A
whitening approach to probabilistic canonical correlation analysis for
omics data integration", <doi:10.1186/s12859-018-2572-9>.

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
