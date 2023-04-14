%global __brp_check_rpaths %{nil}
%global packname  TauStar
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Efficient Computation and Testing of the Bergsma-Dassios SignCovariance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Computes the t* statistic corresponding to the tau* population coefficient
introduced by Bergsma and Dassios (2014) <DOI:10.3150/13-BEJ514> and does
so in O(n^2) time following the algorithm of Heller and Heller (2016)
<arXiv:1605.08732> building off of the work of Weihs, Drton, and Leung
(2016) <DOI:10.1007/s00180-015-0639-x>. Also allows for independence
testing using the asymptotic distribution of t* as described by Nandy,
Weihs, and Drton (2016) <arXiv:1602.04387>.

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
