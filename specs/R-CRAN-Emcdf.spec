%global packname  Emcdf
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Computation and Visualization of Empirical Joint Distribution(Empirical Joint CDF)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-lattice 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-lattice 
Requires:         R-methods 

%description
Computes and visualizes empirical joint distribution of multivariate data
with optimized algorithms and multi-thread computation. There is a faster
algorithm using dynamic programming to compute the whole empirical joint
distribution of a bivariate data. There are optimized algorithms for
computing empirical joint CDF function values for other multivariate data.
Visualization is focused on bivariate data. Levelplots and wireframes are
included.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
