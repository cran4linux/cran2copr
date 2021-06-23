%global __brp_check_rpaths %{nil}
%global packname  wv
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Wavelet Variance

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-simts 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-simts 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides a series of tools to compute and plot quantities related to
classical and robust wavelet variance for time series and regular
lattices. More details can be found, for example, in Serroukh, A., Walden,
A.T., & Percival, D.B. (2000) <doi:10.2307/2669537> and Guerrier, S. &
Molinari, R. (2016) <arXiv:1607.05858>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/dwt_sim.R
%doc %{rlibdir}/%{packname}/modwt_sim.R
%doc %{rlibdir}/%{packname}/sp_modwt_rough.R
%doc %{rlibdir}/%{packname}/test_wvar.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
