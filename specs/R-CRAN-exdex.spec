%global packname  exdex
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Estimation of the Extremal Index

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-chandwich 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-chandwich 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppRoll 
Requires:         R-stats 

%description
Performs frequentist inference for the extremal index of a stationary time
series.  Two types of methodology are used.  One type is based on a model
that relates the distribution of block maxima to the marginal distribution
of series and leads to the semiparametric maxima estimators described in
Northrop (2015) <doi:10.1007/s10687-015-0221-5> and Berghaus and Bucher
(2018) <doi:10.1214/17-AOS1621>.  Sliding block maxima are used to
increase precision of estimation. The other type of methodology uses a
model for the distribution of threshold inter-exceedance times (Ferro and
Segers (2003) <doi:10.1111/1467-9868.00401>). Two versions of this type of
approach are provided, following Suveges (2007)
<doi:10.1007/s10687-007-0034-2> and Suveges and Davison (2010)
<doi:10.1214/09-AOAS292>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
