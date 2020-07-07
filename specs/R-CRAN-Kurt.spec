%global packname  Kurt
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Performs Kurtosis-Based Statistical Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-polynom >= 1.4.0
BuildRequires:    R-CRAN-labstatR >= 1.0.9
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
BuildRequires:    R-CRAN-expm >= 0.999.4
Requires:         R-CRAN-polynom >= 1.4.0
Requires:         R-CRAN-labstatR >= 1.0.9
Requires:         R-CRAN-matrixcalc >= 1.0.3
Requires:         R-CRAN-expm >= 0.999.4

%description
Computes measures of multivariate kurtosis, matrices of fourth-order
moments and cumulants, kurtosis-based projection pursuit. Franceschini, C.
and Loperfido, N. (2018, ISBN:978-3-319-73905-2). "An Algorithm for
Finding Projections with Extreme Kurtosis". Loperfido, N.
(2017,ISSN:0024-3795). "A New Kurtosis Matrix, with Statistical
Applications".

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
