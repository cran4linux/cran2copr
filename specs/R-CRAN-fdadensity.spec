%global packname  fdadensity
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Functional Data Analysis for Density Functions by Transformationto a Hilbert Space

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-fdapace >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-fdapace >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.11.5

%description
An implementation of the methodology described in Petersen and Mueller
(2016) <doi:10.1214/15-AOS1363> for the functional data analysis of
samples of density functions.  Densities are first transformed to their
corresponding log quantile densities, followed by ordinary Functional
Principal Components Analysis (FPCA).  Transformation modes of variation
yield improved interpretation of the variability in the data as compared
to FPCA on the densities themselves.  The standard fraction of variance
explained (FVE) criterion commonly used for functional data is adapted to
the transformation setting, also allowing for an alternative
quantification of variability for density data through the Wasserstein
metric of optimal transport.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
