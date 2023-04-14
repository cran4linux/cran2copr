%global __brp_check_rpaths %{nil}
%global packname  nmixgof
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Goodness of Fit Checks for Binomial N-Mixture Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-unmarked 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-unmarked 

%description
Provides residuals and overdispersion metrics to assess the fit of
N-mixture models obtained using the package 'unmarked'. Details on the
methods are given in Knape et al. (2017) <doi:10.1101/194340>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
